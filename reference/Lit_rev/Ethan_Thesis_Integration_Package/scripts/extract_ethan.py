from pathlib import Path
import fitz,re,csv,json,hashlib,shutil,html
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT
SRC=ROOT/'Ethan_Rozak_Thesis_Original.pdf'
doc=fitz.open(SRC)
for d in ['pages','embedded_images','equation_context','figure_pages','tables','data','scripts']: (OUT/d).mkdir(parents=True,exist_ok=True)
# Original PDF is already in this package.
# Full_Text.txt is already in this package.
eqs=[];figs=[];rasters=[];tables=[];pageindex=[]
current='Front matter'
for i,p in enumerate(doc):
 n=i+1;t=p.get_text(); printed=n-14 if n>=15 else ('i' if n==2 else 'front matter')
 blocks=p.get_text('dict')['blocks']; lines=[]
 for b in blocks:
  for line in b.get('lines',[]):
   text=''.join(s['text'] for s in line['spans']);lines.append((fitz.Rect(line['bbox']),text))
 # Every page is rendered: this preserves vector plots, raster images, and unnumbered mathematics.
 p.get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(OUT/f'pages/pdf_page_{n:03}.png')
 pageindex.append({'pdf_page':n,'printed_page':printed,'text_characters':len(t),'render':f'pages/pdf_page_{n:03}.png'})
 (OUT/'pages'/f'pdf_page_{n:03}.txt').write_text(t)
 labels=[(r,txt.strip()[1:-1]) for r,txt in lines if re.fullmatch(r'\((?:\d+|[A-Z])\.\d+\)',txt.strip())]
 for r,ident in labels:
  # Context image is deliberately generous. Original full page is authoritative.
  top=max(50,r.y0-110);bottom=min(748,r.y1+12)
  path=f'equation_context/eq_{ident.replace(".","_")}_pdf_{n:03}.png'
  p.get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(65,top,548,bottom),alpha=False).save(OUT/path)
  eqs.append({'equation':ident,'pdf_page':n,'printed_page':printed,'context_image':path,'page_image':f'pages/pdf_page_{n:03}.png','source_text_context':p.get_textbox(fitz.Rect(65,top,548,bottom))})
 # Caption matches only body pages; contents/lists excluded.
 if n>16:
  for r,txt in lines:
   m=re.match(r'^Figure\s+([\dA-Z]+\.\d+):\s*(.*)',txt)
   if m:
    ident=m.group(1);figs.append({'figure':ident,'pdf_page':n,'printed_page':printed,'caption_first_line':m.group(2),'page_png':f'pages/pdf_page_{n:03}.png','vector_page_pdf':f'figure_pages/figure_{ident.replace(".","_")}_pdf_{n:03}.pdf','attribution':'See original caption and surrounding text; third-party attribution retained in source page.'})
    one=fitz.open();one.insert_pdf(doc,from_page=i,to_page=i);one.save(OUT/figs[-1]['vector_page_pdf']);one.close()
   mt=re.match(r'^Table\s+([\dA-Z]+\.\d+):\s*(.*)',txt)
   if mt:tables.append({'table':mt.group(1),'pdf_page':n,'printed_page':printed,'caption_first_line':mt.group(2),'page_image':f'pages/pdf_page_{n:03}.png','text_file':f'pages/pdf_page_{n:03}.txt'})
 # Native raster streams, one entry per resource occurrence and source page; includes masks metadata.
 for j,info in enumerate(p.get_images(full=True),1):
  xref,smask=info[:2];data=doc.extract_image(xref);path=f'embedded_images/pdf_{n:03}_image_{j:02}_xref_{xref}.{data["ext"]}'
  (OUT/path).write_bytes(data['image'])
  row={'pdf_page':n,'printed_page':printed,'image_index':j,'xref':xref,'soft_mask_xref':smask,'width':data['width'],'height':data['height'],'file':path,'sha256':hashlib.sha256(data['image']).hexdigest()}
  if smask:
   base=fitz.Pixmap(doc,xref);mask=fitz.Pixmap(doc,smask)
   try:
    rgba=fitz.Pixmap(base,mask);ap=f'embedded_images/pdf_{n:03}_image_{j:02}_composited.png';rgba.save(OUT/ap);row['composited_file']=ap
   except Exception as e:row['mask_note']=str(e)
  rasters.append(row)
for name,rows in [('equations_detected',eqs),('figures',figs),('embedded_images',rasters),('tables',tables),('pages',pageindex)]:
 (OUT/'data'/f'{name}.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
 if rows:
  keys=list(dict.fromkeys(k for r in rows for k in r));
  with (OUT/'data'/f'{name}.csv').open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
# Visual inventory: all numbered equation pages, not tiny equation OCR.
for batch in range(0,len(eqs),12):
 selected=eqs[batch:batch+12];sheet=Image.new('RGB',(1500,12//3*265),'white');draw=ImageDraw.Draw(sheet)
 for k,e in enumerate(selected):
  im=Image.open(OUT/e['context_image']);im.thumbnail((490,230));x=(k%3)*500;y=(k//3)*265
  draw.text((x+8,y+5),f"Eq {e['equation']} | PDF {e['pdf_page']} | printed {e['printed_page']}",fill='black');sheet.paste(im,(x,y+28))
 (ROOT/'tmp').mkdir(exist_ok=True);sheet.save(ROOT/f'tmp/equation_contact_{batch//12+1}.jpg')
summary={'pages':len(doc),'numbered_equations':len(eqs),'figure_captions':len(figs),'embedded_raster_resources_by_page':len(rasters),'tables':len(tables),'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest()}
(OUT/'data/extraction_summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary))
