################## Trident Acu TH Loop Draft Script
### First Created: 01 September 2026
# ⭐⭐ Today editing: 01 September 2026
# 
# 
#                             Reduced SAM Model - Base case for single Phase

# - Goals -
#  Using real HTC BC, not fixed outlet temperature
#  
## Overview questions
#  
# 
#### 
# Using Design docs in box 
#############################  Experimental Prameters and Boundary condition  ######################################################

# Initial Condition
p_0 = 1.1e5 # 1.01e5 # try change to 1.5 or 2 # Initial pressure, and ambient
T_0 = 442 # T_0 = T_c # 441.37 # 430
v_0 = 0.02 # 0.0185
# Boundary Condition
T_amb = 300
h_amb = 12.224 ## FIXME # Will need to do something smart with this. The issue is internal and external Nu. 

# Top left exit pipe (TLEP) settings ###
T_top_out = 442 # approx temp of fluid in top experimental tank, top-left
p_top_out = 1.01e5 # exp tank top left pressure # FIXME later: Suggestion to put it somewhere boring
# Bottom Right Exit Pipe (brep) 
T_bott_out = 450 
p_bott_out =  1.48e5 #1.46981e5 #  rho = 2000, g = 9.81, h = 1.27

######### Heat BC #########
q_heater = 189.26 # W # This is Q_heater 
q_cooler_removal = 90 # W  # Initially, for SS, externally impose. When doing transient, will need something more clever like forced convection or restart simulation with dynamic steps.

#########  Hydraulic BC ######### 
fric_factor = 0.612 ## Global param
# Corner Losses # 
k_brc = 1.8
k_blc = 1.8
k_tlc = 1.8
k_trc = 1.8
k_tlep = 1e3 # high to stop the flow from transporting that way
k_brep = 100 # needs to be high


##################################### Quadrature Settings #####################################
p_order_quadPnts = 2 # 1
quad_type = GAUSS # TRAP
quad_order = SECOND # SECOND # FIRST
scheme =  implicit-euler # BDF2 #    # # crank-nicolson # 



#############################   Geometry Control Panel      ######################################################



# Geometry  and Positions

# Main Loop
horiz_pipe_length =  1.313 # m # ~Gentry
vertical_height   =  1.269 # m # ~Gentry

  # bottom_total_len  = 1.44395 # m
  # top_total_len     = 1.44477 # m
  # up_total_len      = 1.39954 # m
  # down_total_len    = 1.39918 # m

# main piping
pipe_ID = 0.0266 # m, twice the radius, note
pipe_OD = 0.0334 # # m,  2 * 1.67 
pipe_wall_thickness = ${fparse (pipe_OD - pipe_ID) / 2.0}

incl_deg = 7.58 # deg
incl_rad = ${fparse incl_deg * pi/180} # rad

## cooling Jacket ##
  # jacket_OD = 0.1588 # m Gentry 3D model
  # jacket_ID = 0.1492 # m Gentry #
#   jacket_length = 1.016 # m Gentry


## Heater length
heater_length = 1.234 # m


# Exp tank lengths
top_tank_height       =  ${fparse 0.0254 * 44.85} # m, D000158 rev A,            44.85 in = 113.919 cm
bot_drain_tank_height =  ${fparse 0.0254 * 33.43} # m,  D000164 rev A           33.43 in = 84.9122 cm
# top_left_exit_pipe (tlep) #
#     Centerline 3.658 in away from left end of loop (subtract out outer-radius) FIXME: are they still using these values? 
tlep_ID     = ${fparse 0.0254 * 1.278} # m,  D000118 rev A                    1.278 in = 3.24612 cm
tlep_OD     = ${fparse 0.0254 * 1.656} # m,  D000118 rev A                    1.656 in = 4.20624 cm
tlep_length = ${fparse 0.0254 * 8.0}   # m,  D000118 rev A                    8     in = 20.32   cm 
# bottom_right_exit_pipe (brep)
brep_ID     = ${fparse 0.0254 * 1.278} # m,  D000118 rev A                    1.278 in = 3.24612 cm
brep_OD     = ${fparse 0.0254 * 1.656} # m,  D000118 rev A                    1.656 in = 4.20624 cm # 
brep_length = ${fparse 0.0254 * 31.5}  # m,  D000118 rev A                 



############################       Nodes and Geometry      ######################################################

end_pipe_up         = '0    0                                                                       ${fparse (vertical_height) }'
end_cooling_jacket  = '0    ${fparse (horiz_pipe_length) * cos(incl_rad)}                           ${fparse  vertical_height  - 1 * horiz_pipe_length * sin(incl_rad)}'
end_downcomer       = '0    ${fparse (horiz_pipe_length) * cos(incl_rad) }                          ${fparse   - 1*(horiz_pipe_length * sin(incl_rad)) }'
end_heater          = '0    0   0'  # horiz_pipe_length - pre_H_l - heater_length = post_H_l

###### Under the hood -- Making usable ######## 
heater_volumetric_power = ${fparse ${q_heater} / ( (pipe_ID^2 * pi/4) * ${horiz_pipe_length})} # # Volumetric # Watts / m^3 # m^3
cooler_volumetric_power = ${fparse ${q_cooler_removal} / ( (pipe_ID^2 * pi/4)* ${horiz_pipe_length} )}


node_multiplier = 1 # 1 = ~1 node / 10 cm ; 10 = ~1 node / cm

nodes_long  =   ${fparse 14 * node_multiplier} # 140 cm heights #
midnode_med =   ${fparse  7 * node_multiplier} # 70
node_short  =   ${fparse  2 * node_multiplier} # 20 cm


#############################       Control Panel      ######################################################

[GlobalParams]
  global_init_P = ${p_0}                      # I think this is ambient pressure # Global initial fluid pressure # --> Depends on problem, IC to make problem converge, changing IC and scaling factor to make converge
  global_init_V = ${v_0} # Probably shouldnt start with zero velocity, and in loop they defined 1.5 originally             # Global initial fluid velocity
  global_init_T = ${T_0} # Kelvin # Starting water luke-warm           # I am pretty sure SAM uses Kelvin          # Global initial temperature for fluid and solid

  p_order = ${p_order_quadPnts} # 1 # Specifies the order of mesh... How many quadrature points in FE sol # P order 1 runs faster but not as accurate
  gravity = '0 0 -9.8' 

  # Trying debug
  f = ${fric_factor} #6.5 # Use global friction factor
[]
#############################       Materials           ######################################################

  [EOS] # FIXME: Will need to update with the EOS from whatever CFD folk choose
    [eos] #hitec # active eos should be called eos

      type = TabulatedEquationOfState 
      interp_type = Linear 
      temperature = '  381.     	382.     	383.     	384.     	385.     	386.     	387.     	388.     	389.     	390.     	391.     	392.     	393.     	394.     	395.     	396.     	397.     	398.     	399.     	400.     	401.     	402.     	403.     	404.     	405.     	406.     	407.     	408.     	409.     	410.     	411.     	412.     	413.     	414.     	415.     	416.     	417.     	418.     	419.     	420.     	421.     	422.     	423.     	424.     	425.     	426.     	427.     	428.     	429.     	430.     	431.     	432.     	433.     	434.     	435.     	436.     	437.     	438.     	439.     	440.     	441.     	442.     	443.     	444.     	445.     	446.     	447.     	448.     	449.     	450.     	451.     	452.     	453.     	454.     	455.     	456.     	457.     	458.     	459.     	460.     	461.     	462.     	463.     	464.     	465.     	466.     	467.     	468.     	469.     	470.     	471.     	472.     	473.     	474.     	475.     	476.     	477.     	478.     	479.     	480.     	481.     	482.     	483.     	484.     	485.     	486.     	487.     	488.     	489.     	490.     	491.     	492.     	493.     	494.     	495.     	496.     	497.     	498.     	499.     	500.     	501.     	502.     	503.     	504.     	505.     	506.     	507.     	508.     	509.     	510.     	511.     	512.     	513.     	514.     	515.     	516.     	517.     	518.     	519.     	520.     	521.     	522.     	523.     	524.     	525.     '
      mu  =         '2.848E-02	2.814E-02	2.781E-02	2.749E-02	2.716E-02	2.684E-02	2.653E-02	2.621E-02	2.590E-02	2.559E-02	2.528E-02	2.498E-02	2.468E-02	2.438E-02	2.408E-02	2.379E-02	2.350E-02	2.321E-02	2.293E-02	2.264E-02	2.236E-02	2.209E-02	2.181E-02	2.154E-02	2.127E-02	2.100E-02	2.074E-02	2.048E-02	2.022E-02	1.996E-02	1.971E-02	1.945E-02	1.920E-02	1.896E-02	1.871E-02	1.847E-02	1.823E-02	1.799E-02	1.776E-02	1.752E-02	1.729E-02	1.707E-02	1.684E-02	1.662E-02	1.640E-02	1.618E-02	1.596E-02	1.575E-02	1.554E-02	1.533E-02	1.512E-02	1.492E-02	1.471E-02	1.451E-02	1.431E-02	1.412E-02	1.392E-02	1.373E-02	1.354E-02	1.336E-02	1.317E-02	1.299E-02	1.281E-02	1.263E-02	1.245E-02	1.227E-02	1.210E-02	1.193E-02	1.176E-02	1.160E-02	1.143E-02	1.127E-02	1.111E-02	1.095E-02	1.079E-02	1.064E-02	1.049E-02	1.033E-02	1.019E-02	1.004E-02	9.893E-03	9.750E-03	9.608E-03	9.469E-03	9.331E-03	9.195E-03	9.061E-03	8.929E-03	8.798E-03	8.669E-03	8.542E-03	8.417E-03	8.294E-03	8.172E-03	8.052E-03	7.934E-03	7.817E-03	7.702E-03	7.589E-03	7.477E-03	7.367E-03	7.259E-03	7.152E-03	7.047E-03	6.944E-03	6.842E-03	6.741E-03	6.643E-03	6.545E-03	6.450E-03	6.356E-03	6.263E-03	6.172E-03	6.082E-03	5.994E-03	5.907E-03	5.822E-03	5.738E-03	5.656E-03	5.575E-03	5.495E-03	5.417E-03	5.341E-03	5.265E-03	5.191E-03	5.118E-03	5.047E-03	4.977E-03	4.908E-03	4.841E-03	4.775E-03	4.710E-03	4.646E-03	4.584E-03	4.522E-03	4.463E-03	4.404E-03	4.346E-03	4.290E-03	4.235E-03	4.181E-03	4.128E-03	4.076E-03	4.026E-03	3.976E-03'
      rho =         '2.008E+03	2.007E+03	2.006E+03	2.006E+03	2.005E+03	2.004E+03	2.003E+03	2.003E+03	2.002E+03	2.001E+03	2.000E+03	2.000E+03	1.999E+03	1.998E+03	1.997E+03	1.997E+03	1.996E+03	1.995E+03	1.994E+03	1.994E+03	1.993E+03	1.992E+03	1.991E+03	1.991E+03	1.990E+03	1.989E+03	1.988E+03	1.988E+03	1.987E+03	1.986E+03	1.985E+03	1.985E+03	1.984E+03	1.983E+03	1.982E+03	1.982E+03	1.981E+03	1.980E+03	1.979E+03	1.979E+03	1.978E+03	1.977E+03	1.976E+03	1.976E+03	1.975E+03	1.974E+03	1.973E+03	1.973E+03	1.972E+03	1.971E+03	1.970E+03	1.970E+03	1.969E+03	1.968E+03	1.967E+03	1.967E+03	1.966E+03	1.965E+03	1.964E+03	1.964E+03	1.963E+03	1.962E+03	1.961E+03	1.961E+03	1.960E+03	1.959E+03	1.958E+03	1.958E+03	1.957E+03	1.956E+03	1.955E+03	1.955E+03	1.954E+03	1.953E+03	1.952E+03	1.952E+03	1.951E+03	1.950E+03	1.949E+03	1.949E+03	1.948E+03	1.947E+03	1.946E+03	1.946E+03	1.945E+03	1.944E+03	1.943E+03	1.943E+03	1.942E+03	1.941E+03	1.940E+03	1.940E+03	1.939E+03	1.938E+03	1.937E+03	1.937E+03	1.936E+03	1.935E+03	1.934E+03	1.934E+03	1.933E+03	1.932E+03	1.931E+03	1.931E+03	1.930E+03	1.929E+03	1.929E+03	1.928E+03	1.927E+03	1.926E+03	1.926E+03	1.925E+03	1.924E+03	1.923E+03	1.923E+03	1.922E+03	1.921E+03	1.920E+03	1.920E+03	1.919E+03	1.918E+03	1.917E+03	1.917E+03	1.916E+03	1.915E+03	1.914E+03	1.914E+03	1.913E+03	1.912E+03	1.911E+03	1.911E+03	1.910E+03	1.909E+03	1.908E+03	1.908E+03	1.907E+03	1.906E+03	1.905E+03	1.905E+03	1.904E+03	1.903E+03	1.902E+03	1.902E+03	1.901E+03	1900.01  '
      cp  =         '2.730E+03	2.724E+03	2.719E+03	2.714E+03	2.709E+03	2.703E+03	2.698E+03	2.693E+03	2.688E+03	2.683E+03	2.677E+03	2.672E+03	2.667E+03	2.662E+03	2.657E+03	2.652E+03	2.647E+03	2.642E+03	2.636E+03	2.631E+03	2.626E+03	2.621E+03	2.616E+03	2.611E+03	2.606E+03	2.601E+03	2.596E+03	2.592E+03	2.587E+03	2.582E+03	2.577E+03	2.572E+03	2.567E+03	2.562E+03	2.557E+03	2.553E+03	2.548E+03	2.543E+03	2.538E+03	2.534E+03	2.529E+03	2.524E+03	2.519E+03	2.515E+03	2.510E+03	2.505E+03	2.501E+03	2.496E+03	2.491E+03	2.487E+03	2.482E+03	2.478E+03	2.473E+03	2.468E+03	2.464E+03	2.459E+03	2.455E+03	2.450E+03	2.446E+03	2.441E+03	2.437E+03	2.433E+03	2.428E+03	2.424E+03	2.419E+03	2.415E+03	2.411E+03	2.406E+03	2.402E+03	2.398E+03	2.393E+03	2.389E+03	2.385E+03	2.380E+03	2.376E+03	2.372E+03	2.368E+03	2.363E+03	2.359E+03	2.355E+03	2.351E+03	2.347E+03	2.343E+03	2.339E+03	2.334E+03	2.330E+03	2.326E+03	2.322E+03	2.318E+03	2.314E+03	2.310E+03	2.306E+03	2.302E+03	2.298E+03	2.294E+03	2.290E+03	2.286E+03	2.282E+03	2.278E+03	2.275E+03	2.271E+03	2.267E+03	2.263E+03	2.259E+03	2.255E+03	2.252E+03	2.248E+03	2.244E+03	2.240E+03	2.236E+03	2.233E+03	2.229E+03	2.225E+03	2.222E+03	2.218E+03	2.214E+03	2.211E+03	2.207E+03	2.203E+03	2.200E+03	2.196E+03	2.193E+03	2.189E+03	2.186E+03	2.182E+03	2.179E+03	2.175E+03	2.172E+03	2.168E+03	2.165E+03	2.161E+03	2.158E+03	2.154E+03	2.151E+03	2.148E+03	2.144E+03	2.141E+03	2.138E+03	2.134E+03	2.131E+03	2.128E+03	2.124E+03	2.121E+03	2.118E+03	2114.560 '
      
      k   =          '0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.54	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.55	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56	0.56'
    [] 
    
    [air_eos]
      type = AirEquationOfState # HeEquationOfState # # N, He, Na
    []
  []

  [MaterialProperties] # FIXME: Confirm that VCU is using these Mat props as well
    [ss-mat] # my HX is SS 315, manual says ss HT9 and D9 are implemented, but I dont see an example on how to use D9... D9 looks like closest to SS-316... constant is probably faster though 
      type = SolidMaterialProps # Should I use 
      k = 15 # K ranges from (13 - 17) https://www.azom.com/properties.aspx?ArticleID=863
      Cp = 500 # 638 # Ranges from 490 - 530
      rho = 7.7e3 # Density is reported to range from 7.87e3 to 8.07e3... 
    []

    # [water_fp] # used for EOS
    #   type = Water97FluidProperties
    # []
  []

#############################       Geometry           ######################################################


[ComponentInputParameters] # used when you have repeated components, so you dont have to type as much
  
  [ss_pipe_cooling] # used for cooling jacket. Has n_wall_elems that may be worth changing at some point
    type = PBPipeParameters
    eos = eos
    A = ${fparse pi* (pipe_ID)^2 / 4 } # I think cross-sectional area. Does this need to match test section? Can rest be same diameter except for TS? # 0.0003835 # m^2# 
    Dh = ${fparse pipe_ID} # #  Hydraulic diameter, 4*A / p = D # D000118 rev A | Items 2, 3
    hs_type = cylinder
    n_wall_elems = '3' # '3' # num of radial elements in the pipe wall, not the fluid    
    wall_thickness = ${fparse pipe_wall_thickness} #  
    material_wall = 'ss-mat'
  []
  [flow_channel]
    type = PBOneDFluidComponentParameters
    eos = eos
    A = ${fparse pi* (pipe_ID)^2 / 4 }  # I think cross-sectional area. Does this need to match test section? Can rest be same diameter except for TS? # 0.0003835 # m^2# 
    Dh = ${fparse pipe_ID} # 0.0266446 # 1.049*0.0254 #  Hydraulic diameter, 4*A / p = D # D000118 rev A | Items 2, 3
  [] # FIXME: Question: can we use this for input and avoid having to rewrite many things like area and Dh? 
  
  # FIXME: make input parameters for main pipe stainless steel
[]  


[Components] # Geometry

  # Idea💡: Switch from PBOneDFluidComponent to PBPipe if you want to simulate the pipe wall, insulation, and ambient heat loss. 
    #  Will need to create a wall thermal circuit model. 
    
  ######## Main pipes
  [up1]
    type = PBOneDFluidComponent # PBPipe # Updating with what Jadyn used
    input_parameters = flow_channel # this may need to be removed bc no longer pipe # Meaning I would heed to add A and Dh back in probably
    eos = eos # should be able to comment this out
    position = '0 0 0'
    orientation = '0 0 1'
    length = ${fparse vertical_height }  # 
    n_elems = ${nodes_long} # number of axial elements in direction of flow # If you change this, change postprocessor TS_TP
  []
  
  [CoolingJacket] # Note: Entire top leg currently modeled as cooling jacket
    # If we wanted to fix, design docs not clear, but the HX may be ~48.75 in long.  
    type = PBOneDFluidComponent # PBPipe #  Jadyn coupled a heat structure on pipe wall... why not just use pipe? 
    input_parameters =  flow_channel # # ss_pipe_cooling #  # FIXME: Depends on how we model heat loss, may be a boundary condition. Still need to figure out thermal circuit
    eos = eos
    position =   ${end_pipe_up}
    orientation =  '0  ${fparse cos(incl_rad)}  ${fparse -1 * sin(incl_rad)}' # 

    length = ${fparse  horiz_pipe_length} # m 
    n_elems = ${nodes_long} # # 1m

      # Idea💡: Model cooling heat loss with external boundary condition and just force a heat flux 
        # in sourcecode  can go to SAM/tests/ --> regression tests have ex of diff model and components; can look at PBPipe tests for more examples 
    heat_source = ${cooler_volumetric_power} # Instead of heat source, want BC on outside of wall;  # Change to flux BC
      # HS_BC_type = 'Convective' # 'Adiabatic'
      # T_amb = ${T_amb}
      # h_amb = ${h_amb} # HTC
      # Hw = ${h_amb} # can be const or function of space and time
  []
  
  [downcomer]
    type = PBOneDFluidComponent
    eos = eos
    position = ${end_cooling_jacket}
    orientation = '0 0 -1'
    input_parameters = flow_channel
    length =  ${fparse (vertical_height)}
    n_elems = ${nodes_long}
  []

  [Heater] # For an external heating, consider changing to wall heat flux; 
    type = PBOneDFluidComponent 
    eos = eos
    position =    ${end_downcomer}
    orientation = '0  ${fparse -1*cos(incl_rad)}   ${fparse sin(incl_rad)}' # Assuming in radians, 20*
    input_parameters = flow_channel

    length = ${fparse horiz_pipe_length } # meters
    n_elems = ${nodes_long}
    heat_source = ${heater_volumetric_power} # volumetric heat source # average over fluid volume 👁️👁️ # May need to be fixed/changed
  []
  
  ######### Experimental Tanks & BCs
  
  [tlep]
    type = PBOneDFluidComponent
    eos = eos
    position = ${end_pipe_up}
    orientation = '0 0 1'
    A = ${fparse pi* (tlep_ID)^2 / 4 }
    Dh = ${fparse tlep_ID} 
    length =  ${fparse (tlep_length)}
    n_elems = ${node_short} # ~20cm
    # FIXME: Can have Boundary condition like heat loss. However, pinning temperature might work best. 
  []

  [brep]
    type = PBOneDFluidComponent
    eos = eos
    position = ${end_downcomer}
    orientation = '0 0 -1'
    A = ${fparse pi* (brep_ID)^2 / 4 }
    Dh = ${fparse brep_ID} 
    length =  ${fparse (brep_length)}
    n_elems = ${midnode_med}
  []

##################   connecting pipes ... ######################
  
  [up_out]
    type = PBBranch
    inputs = 'up1(out)'
    outputs = 'CoolingJacket(in) tlep(in)'
    eos = eos
    K = '0.0 ${fparse k_tlc} ${fparse k_tlep} ' # '0.0 1.8 1e3' 
    Area = ${fparse pi* (pipe_ID)^2 / 4 } 
  []


  [out_J]
    type = PBBranch
    inputs = 'CoolingJacket(out)'
    outputs = 'downcomer(in)'
    eos = eos
    K = '0.0 ${fparse k_trc}' # '0.0 1.8 1e3' 
    Area = ${fparse pi* (pipe_ID)^2 / 4 } 
  []

  [out_downcomer]
    type = PBBranch
    inputs = 'downcomer(out)'
    outputs = 'Heater(in) brep(in)'
    eos = eos
    K = '0.0 ${fparse k_brc} ${fparse k_brep}' # '0.0 1.8 1e3' # FIXME: Friction factor painful. Need to be controllable from top
    Area = ${fparse pi* (pipe_ID)^2 / 4 } 
  []
  

  [heater_out]
    type = PBSingleJunction
    inputs = 'Heater(out)'
    outputs = 'up1(in)'
    K = '0.0 ${fparse k_blc}'
    eos = eos
    Area = ${fparse pi* (pipe_ID)^2 / 4 } 
  []


################# Pinning Boundary conditions
  [tlep_BC_pin]
    type = PBTDV
    input = 'tlep(out)'
    eos = eos
    p_bc = ${p_top_out} # Pressure pin at same P as initial of system... Hopefully no more salt flowing out of system
    T_bc = ${T_top_out} 
  []
  
  [brep_BC_pin]
    type = PBTDV
    input = 'brep(out)'
    eos = eos
    p_bc = ${p_bott_out} # Pressure pin at same P as initial of system... Hopefully no more salt flowing out of system
    T_bc = ${T_bott_out} 
  []
[]



#############################       Post Processor           ######################################################



[Postprocessors] # Will need to fix some of these... 
  # active = 'dt'
  [massFlowRate]                                      # Output mass flow rate at inlet of TS
    type = ComponentBoundaryFlow
    input = up1(in)
  []

  [velocity]                                  # Output velocity at inlet of CH1
    type = ComponentBoundaryVariableValue
    variable = velocity
    input = up1(in)
  []

   [downcomer_out_velocity]                                  # Output velocity at inlet of CH1
    type = ComponentBoundaryVariableValue
    variable = velocity
    input = downcomer(out)
  []
  [dt]
    type = TimestepSize
  []

  # [TS_vel]                    # Was not able to get this running :(
  #   type = ComponentNodalVariableValue
  #   input = up1(${midnode_long}) 
  #   variable = velocity
  # []



  # [delta_Temp_TP6-TP2]
  #   type = ParsedPostprocessor
  #   pp_names = 'TP6 TP2'
  #   expression = 'TP6 - TP2'
  # []

  [coolingJacket_T_in_primary]                                  # Temperature at IHX inlet
    type = ComponentBoundaryVariableValue
    variable = temperature
    input = CoolingJacket(in)
  []

  [coolingJacket_T_out_primary]                                  # Temperature at IHX outlet
    type = ComponentBoundaryVariableValue
    variable = temperature
    input = CoolingJacket(out)
  []

  [coolingJacket_delta_T]
    type = ParsedPostprocessor
    expression = 'coolingJacket_T_out_primary - coolingJacket_T_in_primary'
    # pp_symbols = 'T'
    pp_names = 'coolingJacket_T_in_primary coolingJacket_T_out_primary'
  []
  # [00_TS_Pr]
    #   type = ParsedPostprocessor
    #   expression = '(5806 - 10.83*TP_TS + 7.24e-3*TP_TS^2) * (0.4737 - 2.3e-3*TP_TS +3.73e-6*TP_TS^2 - 2.02e-9*TP_TS^3) / (0.78 - 1.25e-3*TP_TS +1.6e-6*TP_TS^2) '
    #   # pp_symbols = 'T'
    #   pp_names = 'TP_TS'
    # []

[]


#############################          Executioner            ######################################################

[Preconditioning] # Advised not to touch these 
  [SMP_PJFNK]
    type = SMP
    full = true
    solve_type = 'PJFNK' 
    petsc_options_iname = '-pc_type -ksp_gmres_restart' # ksp_gmres is the number of nonlinear iterations
    petsc_options_value = 'lu 101' # I don't know what these do, I won't touch them yet
  []
[]

# [Executioner] # Change out once mesh is correct
 #   type = mesh-only
 # []

[Executioner] # Creating timestepper
  type =  Transient #  SAMSegregatedTransient #
  # solve_type = 'PJFNK'  # PJFNK JFNK NEWTON FD LINEAR # no n
  # start_time = 0

  ######################
  end_time = 850 # 1e3 used by Travis # I foolishly changed it to 1e6 seconds and found that it really does not change after 700 seconds for second order... Travis was right
  ######################

  dtmin = 1e-7 # after this point starts diverging
  automatic_scaling = false
  
  scheme = ${scheme}

  # dt = ${const_TS}

  dtmax = 1                   # 3600    # drop dt_max to one second // Make based on courant limit bound <timestepper>
  [TimeStepper]
    type = IterationAdaptiveDT
    optimal_iterations = 10
    iteration_window = 4
    dt = 0.1 # 100
    growth_factor = 1.15     # Step size multiplier if solve is good
    cutback_factor = 0.8     # Step size divisor if solve is poor    
  []

  steady_state_detection = true
  steady_state_tolerance = 1e-10
  
  # These values are a good starting point
  nl_rel_tol = 1e-6
  nl_abs_tol = 1e-6 # -7 # e-6 could be too high, want abs to be couple order magn below rel, charlie suggests e-8
  nl_max_its = 12 # Consider increasing to 20
  l_tol =      1e-8 #5 changed w clarno
  l_max_its = 100

  [Quadrature]
    type =  ${quad_type}  # GAUSS # # For second, do Gauss or simpson # For first, do Trap 
    order = ${quad_order} # SECOND # Needs to be same order as p_order at the very top 
  []
[]



[Outputs]
  print_linear_residuals = false
  perf_graph = true
  checkpoint = true
  # show_var_residual_norms = true
  # show_top_residuals = 3
  
  [out_displaced] # dont need it for these runs
    type = Exodus
    use_displaced = true # always keep true to let mesh look good
    execute_on = 'initial timestep_end'
    sequence = false
  []
  [csv]
    type = CSV
  []
  [console]
    type = Console
    execute_scalars_on = 'none'
  []
[]


