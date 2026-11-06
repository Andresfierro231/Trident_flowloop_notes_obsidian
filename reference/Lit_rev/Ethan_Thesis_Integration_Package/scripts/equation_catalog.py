import json,csv
from pathlib import Path
O=Path(__file__).resolve().parents[1]
# A = essential to integrate/audit; B = useful conditional method; C = background/implementation detail.
DATA=r'''
2.1|F_b=\rho_0 gV|Archimedean buoyant force|C|Textbook physics, cited Greif [13]|N|Background only; use integrated loop buoyancy in our solver.
2.2|F_{net}=(\rho_0-\rho)gV|Net parcel force|C|Textbook physics, cited Greif [13]|N|Does not by itself prescribe net loop circulation.
2.3|\rho(T)\approx\rho_0+(\partial\rho/\partial T)_p(T-T_0)|Density linearization|B|Established approximation, cited [14,15]|kg/m^3|Local linearization; do not impose constant other properties without a sensitivity check.
2.4|\rho(T)\approx\rho_0[1-\beta(T-T_0)]|Boussinesq density relation|B|Established approximation, cited [14,15]|kg/m^3|Our model already retains temperature-dependent properties; no replacement proposed.
3.1|\phi(h)=\phi_{exact}+g_p h^p+O(h^{p+1})|Discretization expansion|A|Richardson/Roache/Celik [12,37,39]|Units of QoI|Asymptotic assumption, not guaranteed by a good fit.
3.2|\epsilon_{21}=\phi_2-\phi_1,\quad\epsilon_{32}=\phi_3-\phi_2|Mesh differences|A|Established verification method [12,37]|Units of QoI|Three settled solutions of the same QoI and physical problem required.
3.3|p_{obs}=\frac{1}{\ln r_{21}}\left\lvert\ln\left\lvert\frac{\epsilon_{32}}{\epsilon_{21}}\right\rvert+q(p_{obs})\right\rvert|Observed order, unequal ratios|A|Celik procedure [12]|dimensionless|Implicit solve; guard zero differences, nonconvergence and non-asymptotic behavior.
3.4|q(p)=\ln\left(\frac{r_{21}^{p}-s}{r_{32}^{p}-s}\right),\quad s=\mathrm{sign}(\epsilon_{32}/\epsilon_{21})|Unequal-ratio correction|A|Celik procedure [12]|dimensionless|Use realized h ratios, not nominal cell targets.
3.5|p_{obs}=\ln\left\lvert\epsilon_{32}/\epsilon_{21}\right\rvert/\ln r|Equal-ratio observed order|A|Richardson/Celik [12,37]|dimensionless|Requires equal ratios and a valid convergence regime; no observed order from two grids.
3.6|\phi_{ext}=\frac{r^{p_{obs}}\phi_1-\phi_2}{r^{p_{obs}}-1}|Richardson extrapolation|A|Established method [12,37]|Units of QoI|Thesis calls estimate phi_exact; it is an extrapolated estimate, not known exact truth.
3.7|GCI_{fine}=\frac{F_s e_a^{21}}{r_{21}^{p_{obs}}-1}|Grid Convergence Index|A|Roache/Celik [12,37]|fraction; multiply by 100 for percent|Three-grid Fs=1.25, two-grid Fs=3 as reported; assumed p must be documented for two-grid use.
3.8|e_a^{21}=\left\lvert(\phi_1^{12}-\phi_2)/\phi_1^{12}\right\rvert|Approximate relative error as printed|A|Celik intended; unusual superscript in source|dimensionless|Source visibly prints phi_1 superscript 12. Intended standard form is abs((phi1-phi2)/phi1); do not propagate undefined superscript into code.
3.9|e_{ext}^{21}=\left\lvert(\phi_{ext}^{12}-\phi_1)/\phi_{ext}^{12}\right\rvert|Extrapolated relative error|A|Established method [12,37]|dimensionless|Superscript 12 labels pair-based extrapolation; define it explicitly.
3.10|AR=GCI_{coarse}/(r_{21}^{p_{obs}}GCI_{fine})\approx1|Asymptotic ratio|A|Established method [12,37]|dimensionless|Consistent triplet and normalization needed; AR near 1 alone is not sufficient verification.
3.11|h=\left[\frac{1}{N}\sum_{i=1}^{N}\Delta V_i\right]^{1/3}|Representative 3D cell size|A|Celik procedure [12]|m|Record geometry/volume changes across meshes; h=(V/N)^(1/3).
3.12|Q=\frac{T_\infty-T_{b,in}}{1/(h_s2\pi r_0L)+\ln(r_1/r_0)/(k_{ss}2\pi L)+\ln(r_2/r_1)/(k_{ins}2\pi L)+1/(h_\infty2\pi r_2L)}|Cylindrical verification circuit|A|Classical resistance network; Ethan applies it|W|Negative for heat leaving hot fluid under Ethan's convention; our outward-positive ledger reverses numerator.
3.13|\overline{Nu}_D=\frac{3.657}{\tanh(2.264Gz^{-1/3}+1.7Gz^{-2/3})}+0.0499Gz\tanh(Gz^{-1})|Thermally developing laminar tube|A|Sellars/Tribus/Klein via Lienhard [45,20]|dimensionless|Constant-wall-temperature, hydrodynamically developed straight-tube reference. Gz=Re Pr D/L. At Gz=3554 gives 23.7336, not appendix 26.67. Not a universal loop correlation.
3.14|E=S-D|Validation comparison error|A|ASME V&V 20 [40]|Same units for S,D|Use observation-matched outputs; signed error is not model uncertainty.
3.15|u_{val}=\sqrt{u_{num}^2+u_{input}^2+u_D^2}|Combined validation uncertainty|A|ASME framework [40]|Units of QoI|RSS assumes commensurate uncertainty components and appropriate independence/covariance treatment. Not automatically a 99% interval.
3.16|L_2=\sqrt{\frac{1}{N}\sum_{i=1}^{N}(S_i-D_i)^2}|Velocity/temperature RMSE|A|Standard statistic; Ethan's application|m/s for velocity; K for temperature|This is RMS error, not unnormalized Euclidean L2 norm. Match sampling points and disclose normalization of percent error.
3.17|L_\infty=\max_i\lvert S_i-D_i\rvert|Maximum absolute discrepancy|B|Standard statistic|m/s or K|Use alongside signed bias and RMS; grid of comparison points matters.
4.1|Q=\dot m c_p(T_{out}-T_{in})|Air cooler duty, constant/mean cp|A|Experimental method from Reis [9]|W|With cp at midpoint it is an approximation to integral cp dT, often very good over this range.
4.2|\rho=2293.6-0.7497T|Legacy HITEC density|A|Reis/Janz [9,26]|kg/m^3; T in K|Same density form retained in 5.15 and our model.
4.3|\mu=0.4737-2.297\times10^{-3}T+3.731\times10^{-6}T^2-2.019\times10^{-9}T^3|Legacy HITEC viscosity|A|Legacy property compilation/Reis [9,26,46]|Pa s; T in K|Reconstruction-only branch; do not replace modern viscosity. Rounded appendix differs appreciably.
4.4|c_p=5806-10.833T+7.2413\times10^{-3}T^2|Legacy HITEC heat capacity|A|Legacy compilation/Reis [9,26,47]|J/(kg K); T in K|Different cp package from our current 1423.47. Retain for explaining historical nondimensional values only.
4.5|k=0.78-1.25\times10^{-3}T+1.6\times10^{-6}T^2|HITEC conductivity|A|Reis/Santini [9,48]|W/(m K); T in K|Same as 5.18; exact coefficient provenance/range remains partly source-limited online.
4.6|\sigma_{Qnet}=Q_{net}\sqrt{(\sigma_{Qh}/Q_h)^2+(\sigma_{Qloss}/Q_{loss})^2}|Net-heat uncertainty as printed|A|Attributed to Reis Eq.25 [9]; Ethan reconstructs|W|Not standard independent propagation for difference Qh-Qloss. Correct absolute RSS is sqrt(sigma_Qh^2+sigma_Qloss^2), with covariance if correlated; use full measurement model for m cp DeltaT.
4.7|Q_{net}=\dot m c_p(TP6-TP2)|Heater-region energy estimate|A|Experimental reduction [9]|W|Must match actual control volume, cp package and sensor/operator. Table4.4 DeltaT row differs from TableC.1 TP6-TP2.
4.8|Q_{loss}=Q_h-Q_{net}|Residual inferred loss|A|Energy accounting, Ethan reconstruction|W|Negative residual is a consistency diagnostic, not proof of unphysical experiment; propagated property/operator errors can cause it.
4.9|U_{PIV}=\frac{2}{R^2}\int_0^R U(r)r\,dr|Axisymmetric PIV-to-area operator|A|Ethan reconstructs experimental processing [9]|m/s|Axisymmetry and use of right-half profile are assumptions; not physical net transport in asymmetric recirculating 3D flow.
4.10|U_\infty=U_{PIV}(D_{test}/D_{pipe})^2|Test-section to pipe velocity conversion|A|Continuity plus Ethan's reconstruction|m/s|Use signed net mass flux for runtime/ROM targets; keep experimental operator separate.
4.11|u_{dig}=1.5\%|Assigned digitization uncertainty|B|Ethan's salt-based reconstruction calibration|percent|Global assigned RMSE bound, not pointwise guarantee: Table4.6 worst RMSE=3.65%, max discrepancy=14.10%.
5.1|\overline{Nu}_L=\left[0.825+\frac{0.387Ra_L^{1/6}}{[1+(0.492/Pr)^{9/16}]^{8/27}}\right]^2|Vertical plate natural convection|A|Churchill-Chu [49]|dimensionless|Uses air properties and characteristic L; vertical-cylinder curvature applicability must be checked.
5.2|\overline{Nu}_D=\left[0.60+\frac{0.387Ra_D^{1/6}}{[1+(0.559/Pr)^{9/16}]^{8/27}}\right]^2|Horizontal-cylinder natural convection|A|Churchill-Chu horizontal-cylinder paper; absent as separate [49] entry|dimensionless|Uses outer insulation diameter and air properties. Add correct horizontal-cylinder citation.
5.3|h_{ext}=\overline{Nu}_{eff}k/D|Nusselt-to-convection coefficient|A|Definition|W/(m^2 K)|For vertical correlation h=Nu_L k/L; do not use D for a vertical Nu_L. Eq5.5's blend of h is safer than a blend of unequal-length Nu values.
5.4|q_{outer}=h_{ext}(T_s-T_\infty)+\epsilon\sigma(T_s^4-T_\infty^4)|Outside convection plus radiation|A|Established heat transfer|W/m^2 outer surface|Use absolute K in radiation; distinguish air temperature and radiative surroundings when available.
5.5|h_{eff}=(1-w)h_{horizontal}+wh_{vertical}|Orientation blend|B|Ethan's engineering interpolation|W/(m^2 K)|w=sin(theta)^2 from horizontal. Not a validated inclined-cylinder law; test endpoints and sensitivity.
5.6|Q_{cooler}=\dot m_{air}[c_p(T_{out})T_{out}-c_p(T_{in})T_{in}]|Cooler formula as printed - correction required|A|Ethan's stated implementation, not valid general enthalpy identity|W|Replace with mdot integral(cp dT). For AppendixB air cp, 25-to-113 C: printed formula +2.1408% vs integral; midpoint cp differs only -0.0292%.
5.7|Q_{heater}+Q_{test\ section}-Q_{cooler}-Q_{passive}-Q_{fins}=Q_{unaccounted}|Global energy ledger|A|Conservation; Ethan's component partition|W|Directly useful; keep prescribed electrical input separate from fluid-delivered heat and each loss category.
5.8|\partial_t\rho+\nabla\cdot(\rho\mathbf U)=0|Variable-density mass conservation|A|Standard governing equation/OpenFOAM|kg/(m^3 s)|Consistent with rho(T), not strictly constant-density divergence-free incompressibility.
5.9|\partial_t(\rho\mathbf U)+\nabla\cdot(\rho\mathbf U\otimes\mathbf U)=-\nabla p_{rgh}-(\mathbf g\cdot\mathbf r)\nabla\rho+\nabla\cdot\tau_{eff}|Buoyant-pressure momentum|A|Standard pressure transformation/OpenFOAM|N/m^3|Reconstruct physical p before pressure-loss reduction; audit g/position reference and signs.
5.10|p_{rgh}=p-\rho\mathbf g\cdot\mathbf r|Pressure decomposition|A|OpenFOAM convention|Pa|Use our actual xref/ghRef; do not compare p_rgh directly with physical static pressure.
5.11|\tau_{eff}=\mu_{eff}[\nabla\mathbf U+(\nabla\mathbf U)^T-\frac23(\nabla\cdot\mathbf U)\mathbf I],\quad\mu_{eff}=\mu+\mu_t|Variable-viscosity effective stress|A|Newtonian/RANS constitutive law|Pa|Our laminar cases set mu_t=0; do not silently introduce turbulence.
5.12|\partial_t(\rho h)+\nabla\cdot(\rho\mathbf U h)+\partial_t(\rho K)+\nabla\cdot(\rho\mathbf U K)-\partial_t p=\nabla\cdot(\alpha_{eff}\nabla h)+\rho\mathbf U\cdot\mathbf g|Enthalpy/kinetic energy equation|B|OpenFOAM-style equation|W/m^3|Check actual solver source/version and h vs internal-energy selection; not a direct ROM equation replacement.
5.13|\alpha_{eff}=\mu/Pr+\mu_t/Pr_t|Enthalpy diffusion coefficient|A|OpenFOAM transport model convention|kg/(m s), not m^2/s|For molecular part alpha_eff=k/cp. Distinguish this dynamic diffusivity from kinematic thermal diffusivity k/(rho cp).
5.14|\rho(T)=\sum_{i=0}^{N}a_iT^i|Polynomial density model|B|OpenFOAM icoPolynomial|kg/m^3|Use actual exported coefficients, interpolation and valid temperature range.
5.15|\rho=2293.6-0.7497T|Current HITEC density|A|Janz [26], as cited by Ethan|kg/m^3; T in K|Our formula matches; PDF p54 nominal temperature has Celsius-to-Kelvin typo.
5.16|\mu=1.149\times10^{-3}\exp(-810.896/T+7.806\times10^5/T^2)|Modern HITEC viscosity|A|Jin et al. [50]|Pa s; T in K|Our formula matches; publisher confirms study/2.5% uncertainty, exact fitted coefficients not independently accessible online.
5.17|c_p\approx1423.47|Modern HITEC constant cp|A|Parida-Basu [51], base salt measurement|J/(kg K)|Primary article reports 1.42347 J/(g K), confirming unit conversion; +/-4% is Ethan's inferred range, not a measured standard uncertainty.
5.18|k=0.78-1.25\times10^{-3}T+1.6\times10^{-6}T^2|Current HITEC conductivity|A|Santini [48], as cited|W/(m K); T in K|Same as4.5. Correct cited year to1984; exact validity and uncertainty need source verification.
5.19|G_b=-C_g\nu_t(\mathbf g\cdot\nabla\rho),\quad C_g=1/Pr_t=1|Buoyant turbulence production|C|Ethan custom codedFvModel|W/m^3 if volumetric rho-k equation|Check source normalization; divide rho for a per-mass k equation. Fixed Pr_t=1 is a modeling choice. Not justified for current laminar ROM by this expression alone.
5.20|n=\left\lfloor\frac{\ln(\Delta_{bulk}/\Delta_1)}{\ln r_{exp}}\right\rfloor+1|Wall-grading cell count|C|Ethan meshing implementation|integer|Confirm floor operation and degenerate rexp=1; preserve realized mesh metrics.
5.21|\delta_{BL}=\Delta_1\frac{r_{exp}^{n}-1}{r_{exp}-1}|Graded-layer thickness|C|Geometric series|m|Handle rexp=1 limit n Delta1; not measured hydrodynamic boundary layer thickness.
5.22|core\_ratio=1-\delta_{BL}/R_{pipe}|O-grid core fraction|C|Ethan meshing implementation|dimensionless|Require 0<core_ratio<1; not a physical closure.
5.23|R_{ps}=\sum_{i=1}^{N}\frac{r_0\ln(r_i/r_{i-1})}{k_i}|Cylindrical resistance normalized to inner area|A|Classical conduction; Ethan BC implementation|m^2 K/W|Essential area normalization; our model already has annular resistance. Variable k layers require integral-consistent discretization.
5.24|q_{out}=\frac{A_{outer}}{A_{inner}}[h_{ext}(T_s-T_a)+\epsilon\sigma(T_s^4-T_{sur}^4)]|Outside loss referred to inner wall|A|Conservation/geometry; Ethan BC|W/m^2 inner surface|Aout/Ain=rout/r0 for equal axial length. Source names qout but uses inner-area basis.
5.25|(T_p-T_s)/R_{ps}=q_{out}|Nonlinear wall closure|A|Classical heat balance; Ethan BC|W/m^2 inner surface|Tp must be fluid-side wall temperature unless internal film resistance is explicitly included. Add layer electrical sources with correct partition, not only this source-free form.
6.1|L_h\approx0.05ReD=0.334\,m|Verification hydrodynamic entry estimate|B|Standard straight-tube estimate; Ethan calculation|m|Correct arithmetic for Re334,D0.02m. Approximate criterion, not proof in junction-rich loop.
6.2|L_t\approx0.05RePrD=17.8\,m|Verification thermal entry estimate|B|Standard straight-tube estimate; Ethan calculation|m|Correct arithmetic; constant-property verification case uses legacy cp and Pr53.2, not modern operating salt cp.
6.3|Q=(T_{amb}-T_f)A_{inner}/(R_{int}+R_{ps}+R_{ext})|Area-normalized verification heat flow|A|Classical resistance network; Ethan application|W|Same sign convention as3.12. Reference is correlation-based for internal film, not exact analytic full PDE solution.
B.1|\phi(T)=\sum_{i=0}^{N}a_iT^i|Generic property polynomial|A|Standard representation|Property-dependent; T in K|Tables B1,B2,B4 are coefficient sets, included as separate unnumbered equation groups; do not silently use legacy B1 over current5.15-18.
'''
meta={e['equation']:e for e in json.loads((O/'data/equations_detected.json').read_text())}
rows=[]
for line in DATA.strip().splitlines():
 ident,latex,title,priority,attribution,units,note=line.split('|')
 def section_of(key):
  if key=='B.1':return 'Appendix B opening'
  ch,num=map(int,key.split('.'))
  if ch==2:return '2.1'
  if ch==3:
   return '3.2' if num<=6 else '3.3' if num<=10 else '3.3.2' if num==11 else '3.4.2' if num<=13 else '3.6' if num<=15 else '3.6.1'
  if ch==4:return '4.2.3' if num==1 else '4.3.1' if num<=5 else '4.5.1' if num<=8 else '4.5.2' if num<=10 else '4.5.3'
  if ch==5:return '5.1.2' if num<=5 else '5.1.3' if num==6 else '5.1.5' if num==7 else '5.2.1' if num<=13 else '5.2.2' if num<=18 else '5.2.3' if num==19 else '5.3.3' if num<=22 else '5.4.2'
  return '6.1.1' if num<=2 else '6.1.2'
 row=dict(meta[ident]);row.update(latex=latex,title=title,priority=priority,attribution=attribution,units=units,use_and_cautions=note,section=section_of(ident),verification_status='Source-page transcription visually checked; primary-source verification and limitations in fact-check register.')
 rows.append(row)
assert set(meta)=={r['equation'] for r in rows},(set(meta)-{r['equation'] for r in rows})
(O/'data/equations.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
with (O/'data/equations.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
with (O/'Equations_Numbered.tex').open('w') as f:
 f.write('% REFERENCE TRANSCRIPTION. Not a drop-in manuscript patch. Source/corrections in equations.json.\n')
 for r in rows:f.write(f"\n% Eq {r['equation']}; PDF {r['pdf_page']}; printed {r['printed_page']}; priority {r['priority']}: {r['title']}\n% {r['use_and_cautions']}\n\\[\n{r['latex']}\n\\]\n")
print(len(rows))
