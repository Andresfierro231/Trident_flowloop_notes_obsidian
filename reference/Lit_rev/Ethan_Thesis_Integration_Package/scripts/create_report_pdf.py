from pathlib import Path
import json,re,html
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether,ListFlowable,ListItem
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
O=Path(__file__).resolve().parents[1]
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DV',font));pdfmetrics.registerFont(TTFont('DV-Bold',bold));pdfmetrics.registerFontFamily('DV',normal='DV',bold='DV-Bold',italic='DV',boldItalic='DV-Bold')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyDV',fontName='DV',fontSize=9.3,leading=14,spaceAfter=8,textColor=colors.HexColor('#172538')))
styles.add(ParagraphStyle(name='TitleDV',fontName='DV-Bold',fontSize=26,leading=33,spaceAfter=16,textColor=colors.HexColor('#164368')))
styles.add(ParagraphStyle(name='H1DV',fontName='DV-Bold',fontSize=17,leading=22,spaceBefore=17,spaceAfter=10,keepWithNext=True,textColor=colors.HexColor('#164368')))
styles.add(ParagraphStyle(name='H2DV',fontName='DV-Bold',fontSize=12,leading=17,spaceBefore=13,spaceAfter=8,keepWithNext=True,textColor=colors.HexColor('#164368')))
styles.add(ParagraphStyle(name='SmallDV',fontName='DV',fontSize=8,leading=12,spaceAfter=7))
story=[]
def clean(s):
 s=str(s).replace('→',' to ').replace('–','-').replace('—','-').replace('−','-').replace('≤','<=').replace('≥','>=').replace('×',' x ')
 # Add separation around common case labels, units, and quoted identifiers in the compact source inventory.
 s=re.sub(r'\b(Salt|Water)([1-4])',r'\1 \2',s)
 s=re.sub(r'(?<=[a-z])(?=[A-Z][a-z])',' ',s)
 s=re.sub(r'\b(PDF|Table|Eq|Fig)(?=\d)',r'\1 ',s)
 s=re.sub(r'(?<=\d)(?=(?:mm|cm|kg|m/s|in\b|W\b|K\b|J/|deg\b))',' ',s)
 replacements={'sourcepage':'source page','case labels31':'case labels 31','actualblockMeshDict':'actual blockMeshDict','reported14':'reported 14','notm2/s':'not m2/s','notknown':'not known','saltTPby':'salt TP by','sourceerrors':'source errors','ownmeshes':'own meshes','RSCprimary':'RSC primary','wallHTC':'wall HTC'}
 for a,b in replacements.items():s=s.replace(a,b)
 return html.escape(s)
def p(s,sty='BodyDV'):story.append(Paragraph(clean(s),styles[sty]))
def label(l,s):story.append(Paragraph('<b>'+clean(l)+':</b> '+clean(s),styles['BodyDV']))
p('Ethan’s thesis to your CFD-to-1D thesis','TitleDV')
p('Evidence-backed integration plan | 20 October 2026','H2DV')
p('Review edition. 24 integration proposals, 22 fact checks, 61 numbered equations, 31 supplemental equation groups, 33 captioned figures and 39 embedded image resources.')
p('The highest-value integration is to improve the provenance and interpretation of your computational reference: reconcile configuration versions, distinguish the PIV measurement operator from conservative transport, strengthen wall and energy verification, and qualify uncertainty claims. Modern HITEC properties, annular heat loss and recirculation motivation are largely already present in your manuscript.')
label('Scope','This report is a reviewable plan. Neither your manuscript nor production model has been modified. Proposed changes require an agreed scope. Numerical checks diagnose the supplied PDF; they are not reruns of Ethan’s unavailable code.')
label('Page convention','Source locations use PDF page indices, starting at 1, plus printed thesis page numbers. For the body and appendices, printed page = PDF page - 14. The title page says May 2026; PDF creation metadata is later and does not determine the degree date.')
label('Controlling comparison','CSEM_Master_s_Dissertation (7)(2).zip, current six-chapter source. Chapters 2-5, air-property appendix, bibliography, README and AGENTS instructions were inspected. No executable simulation archive was supplied. The review therefore gives code behavior and tests instead of inventing exact runtime module paths.')
p('Recommended order','H1DV')
for s in ['1. Resolve configuration, property and observation-operator provenance before transferring numbers.','2. Make documentation and citation corrections; keep frozen results and model definitions intact.','3. Implement independently testable wall, enthalpy and uncertainty diagnostics after locating the exact runtime source.','4. Test one physical variant at a time, with fixed electrical inputs and a declared calibration/test split.','5. Keep water turbulence and pipeline replacement outside the present core scope.']:p(s)
p('Configuration crosswalk','H1DV')
cross=json.loads((O/'data/configuration_crosswalk.json').read_text())
for r in cross:
 p(r['quantity'],'H2DV');label('Your source',r['ours']);label('Ethan',r['ethan']);label('Implication',r['consequence'])
p('Detailed integration proposals','H1DV')
p('P0 denotes a claim or provenance blocker; P1 denotes high-value integration; P2 denotes optional work or work outside present scope. These are proposals, not silently accepted edits.')
for r in json.loads((O/'data/integration_plan.json').read_text()):
 p(f"{r['id']} | {r['priority']} | {r['topic']}",'H2DV')
 for k,l in [('ethan_reference','Source'),('attribution','Attribution'),('evidence_and_insight','Insight'),('compatibility','Compatibility'),('proposed_code_or_thesis_change','Proposed change'),('validation','Validation'),('status','Status')]:label(l,r[k])
p('Numerical evidence and limits','H1DV')
p('Table 6.10, PDF 109 / printed 95, reports the following aggregate comparisons. All mass flows here use piv_method, not a three-dimensional signed mass-flux operator. Wall comparisons use a best-aligned azimuth. Water 2 selects SSTLM_Gb; Water 4 selects SSTLM; remaining cases use laminar results. Reported rounded values are retained in the machine-readable CSV.')
for r in json.loads((O/'data/reported_results_table_6_10.json').read_text()):
 p(r['case']+' | '+r['model'],'H2DV')
 p(f"Mass flow: prediction {r['mdot_sim_kg_s']} kg/s, reported reference {r['mdot_reported_kg_s']} kg/s; error {r['mdot_error_reported_pct']:+.2f}%, adopted validation uncertainty {r['mdot_uval_reported_pct']:.2f}%. Mean fluid-temperature error {r['TPmean_error_reported_K']:+.2f} K with uncertainty {r['TPmean_uval_K']:.2f} K. Wall error {r['TW_error_reported_K']:+.2f} K with uncertainty {r['TW_uval_K']:.2f} K. Ethan’s aggregate verdict: {r['reported_verdict']}.")
p('Seven case labels are reported within adopted bands, but the result is conditional retrospective agreement, not a demonstration of general or prospective accuracy. Aggregate mean temperatures do not establish pointwise temperature agreement. These numerical errors do not transfer to your differently configured CFD reference.')
p('Other reported evidence: composite fins account for 9-16% of modeled heat removal (Section 5.1.4, PDF 69); a 0.1-inch-radius location neighborhood can change salt probe temperatures by more than 10 K (Section 6.4, PDF 99/103); finest-grid integrated power differs from the boundary reference by 0.062-0.067% (Tables 6.2-6.4, PDF 90-91), subject to the reference-Nusselt inconsistency below.')
p('Fact-check register','H1DV')
p('Verification is bounded. Primary publisher and official NIST, ASME and OpenFOAM sources were used. Several full texts were paywalled or blocked; these checks are explicitly partial. This review does not certify every literature statement or simulated result in the thesis. A printed mistake does not establish that the unavailable code used it, and a correct printed formula does not establish that the code implemented it.')
for r in json.loads((O/'data/fact_checks.json').read_text()):
 p(r['id']+' | '+r['status'],'H2DV')
 for k,l in [('ethan_reference','Location'),('claim','Claim'),('check_result','Finding'),('action','Action'),('sources','Evidence')]:label(l,r[k])
p('Most important equations for our work','H1DV')
p('The complete Equation_Inventory.html and CSV/JSON files include all 61 numbered equations, source-page contexts, readable LaTeX, units, attribution and priority. Supplemental unnumbered groups include nondimensional definitions and every property-coefficient family. Source-page images preserve unclassified inline algebra. Priority A means essential to audit or integrate, not automatically approved for production.')
for ids,note in [('3.12; 5.23-5.25','Annular resistance, inner/outer area normalization and nonlinear wall balance. Essential to audit thick insulation and electrical source partition.'),('5.7; 4.7-4.8','Global and segment energy accounting. Essential to distinguish prescribed electrical input, net fluid heat, passive losses and structural paths.'),('4.9-4.10','PIV observation reconstruction. Essential because a planar axisymmetric proxy is not the same operator as conservative net transport.'),('3.1-3.11; 3.14-3.17','Quantity-specific mesh verification, error and uncertainty. Essential, with explicit assumptions for two-grid estimates and coverage.'),('5.15-5.18','Modern HITEC properties, already matched in your source. The conflicting legacy appendix must not override them.'),('3.13; 6.1-6.3','Straight-tube developing-flow benchmark and entrance scales. Useful verification reference under its own assumptions; the appendix Nu must be reconciled.'),('5.1-5.5','External convection and radiation. Keep correct characteristic lengths and identify the inclination blend as an engineering assumption.'),('5.6','Do not adopt as printed. Use mdot times the integral of cp over temperature for an enthalpy difference.')]:label(ids,note)
p('Figures and image extraction','H1DV')
p('Image_Atlas.html links all 33 captioned figures, every one of the 39 page-associated native raster resources, and 139 rendered pages. Each native resource has a page, xref, dimensions and hash. Alpha masks are composited where present. Vector plots are preserved in the original PDF and individual source-page PDF exports. Figure-context PDFs include captions and any neighboring figure; they are not mislabeled as isolated raster originals.')
p('Highest value: Figures 6.10-6.11 (sensor sensitivity), 6.16-6.20 (three-dimensional recirculation), 3.1 (annular circuit), 5.1-5.2 (geometry provenance), and 6.3 (PIV plane). Prefer your own corresponding plots for manuscript figures and cite Ethan for the mechanism or method. Facility photographs/experimental PIV retain Reis attribution. Appendix C captions are repetitive and should not be used alone to identify plot content.')
p('Implementation sequence','H1DV')
for s in ['Documentation first: proposed scope is Chapters 03/04/05 and references.bib, with a configuration crosswalk and exact source locations. Preserve CFD comparison versus experiment and retrospective versus predictive claim boundaries. The later user preference P2-baseline controls the former P2-unity label; do not alter P2-CFD’s target-informed status.','Reproduce before modifying: recover exact runtime commits, dictionaries, geometry and property tables, probe/plane operators, time windows and baseline reports. Add diagnostics before changing physics.','Physical candidates: separate quartz end-ring heating, structural fin losses, sensor positions and convection assumptions. Identify one change at a time against relevant quantities, then hold parameters fixed on withheld cases.','Numerical acceptance: conservation residuals, correct limiting behavior, dimensional consistency, matched operators and quantity-specific verification. Use expanded uncertainty only with a declared coverage model.','Manuscript acceptance: follow repository scope/instructions, build and run the scientific QA scripts after approved changes. No tables or claims are updated from imagined reruns.']:p(s)
p('Unresolved evidence','H1DV')
p('The cause of Salt 1 discrepancy; original PIV processing scripts; wall-probe azimuth/location; quartz ring heating; as-built insulation and material identity; actual code and coefficients behind conflicting appendices; assumed full-loop two-grid convergence order; and exact source correlation uncertainty/ranges where full texts were inaccessible. Codex should retain these as unresolved rather than inventing inputs.')
p('Sources and verification scope','H1DV')
for r in json.loads((O/'data/sources.json').read_text()):
 p(r['id']+' | '+r['title'],'H2DV');label('Checked',r['status']);label('Scope',r['scope'])
 if r.get('url','').startswith('https://'):
  story.append(Paragraph('<link href="'+html.escape(r['url'],quote=True)+'" color="#155e9b">Open primary source</link>',styles['SmallDV']))
  p(r['url'],'SmallDV')
def footer(c,d):
 c.saveState();c.setStrokeColor(colors.HexColor('#ccd7e5'));c.line(47,43,565,43);c.setFont('DV',8);c.setFillColor(colors.HexColor('#53657a'));c.drawString(47,30,'Ethan thesis integration review | 20 October 2026');c.drawRightString(565,30,str(d.page));c.restoreState()
dest=O.parent/'Ethan_Thesis_Integration_Plan.pdf'
SimpleDocTemplate(str(dest),pagesize=(612,792),rightMargin=47,leftMargin=47,topMargin=44,bottomMargin=56,title='Evidence-backed integration plan: Ethan thesis to Andres CFD-to-1D thesis',author='Prepared for Andres Fierro').build(story,onFirstPage=footer,onLaterPages=footer)
print(dest)
