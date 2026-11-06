from pathlib import Path
import math,json,re
O=Path(__file__).resolve().parents[1] if Path(__file__).resolve().parent.name=='scripts' else Path('/workspace/scratch/9525230dbaae/output/Ethan_Thesis_Integration_Package')
def values(T):
 rho=2293.6-.7497*T;mu=.001149*math.exp(-810.896/T+780600/T**2);cp=1423.47;k=.78-.00125*T+1.6e-6*T*T
 return dict(T_K=T,T_C=T-273.15,rho_kg_m3=rho,mu_Pa_s=mu,cp_J_kgK=cp,k_W_mK=k,Pr=mu*cp/k)
c=[1061.3,-.43282,.0010234,-6.4747e-7,1.3864e-10]
cp=lambda t:sum(a*t**i for i,a in enumerate(c))
h=lambda t:sum(a*t**(i+1)/(i+1) for i,a in enumerate(c))
a,b=298.15,386.15
dh=h(b)-h(a);printed=cp(b)*b-cp(a)*a;mid=cp((a+b)/2)*(b-a)
Nu=3.657/math.tanh(2.264*3554**(-1/3)+1.7*3554**(-2/3))+.0499*3554*math.tanh(1/3554)
result=dict(description='Independent arithmetic checks of source statements; not a simulation or experimental reanalysis.',temperature_conversion_C200_to_K=200+273.15,modern_properties=[values(473.15),values(493.15)],cooler=dict(Tin_K=a,Tout_K=b,integral_J_kg=dh,printed_eq5_6_J_kg=printed,midpoint_J_kg=mid,printed_error_pct=100*(printed/dh-1),midpoint_error_pct=100*(mid/dh-1)),Graetz_reference=dict(Gz=3554,Nu_from_eq3_13=Nu,Nu_appendix=26.67,h_recomputed_W_m2K=Nu*.54/.02,Rint_recomputed_m2K_W=1/(Nu*.54/.02)),salt_deltaTP6_minus_TP2_K=[9.26,9.97,9.08,6.8],salt_Qnet_diagnostic_modern_cp_W=[m*1423.47*d for m,d in zip([.0158,.0168,.0175,.0201],[9.26,9.97,9.08,6.8])],geometry_scaling=dict(area_ratio_093_over_087=(.93/.87)**2,velocity_ratio_at_fixed_mdot_rho=(.87/.93)**2,laminar_resistance_ratio_at_fixed_flow=(.87/.93)**4))
assert abs(Nu-23.7335613453)<1e-9
assert abs(result['cooler']['printed_error_pct']-2.1408053221)<1e-8
assert abs(result['modern_properties'][0]['rho_kg_m3']-1938.879445)<1e-8
(O/'data/numerical_checks.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
