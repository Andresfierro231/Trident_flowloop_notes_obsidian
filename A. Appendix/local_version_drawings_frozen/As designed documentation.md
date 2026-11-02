- Not as built *** [[D-000167_PKG.pdf]]
![[D-000167_PKG.pdf|400]]

1. Exp (top) Tank: height 44.85 in - D000158 rev A
2. Drain tank: height 33.43 in  - D000164 rev A 
3. Pipes - SS 3116 
	1. Main piping - -   D000118 rev A | Items 2, 3
		1.  1.049  in ID, 1.315 in OD, % Wall thickness : 
			1. Gentry's [[MainVault/Box/VCU ACU Shared Research/Design_Documentation/Drawings/ACU STNCL Loop Drawings/3D Models/ExtractedMeasurements.txt|ExtractedMeasurements]] from [[ ANEC-000126_06302026.stpz|CAD]] claim:
				1. Pipe ID 1.33 cm; Pipe OD 1.67 cm
				2. See [[Gentry's ACU Flow-Loop Specifications]] ⭐️
		2. Pipe bending can be seen D-000117a [[D-000117a 1.pdf]]
			![[Gentry's ACU Flow-Loop Specifications#Bend Geometry]]
			
	2. Top-Left Exit -   D000118 rev A |  [[D-000118 updated.pdf]]
		1. 1.278 in ID, 1.656 in OD,  % Wall thickness : 0.189 in
		2. 8 in long
		- Center-Line 3.658 in away from left end of loop
	3. Bott-Right exit - D000118 rev A (updated)
		1. 1.278 in ID, 1.656 in OD, 
		2. 31.5 in long
### HX
HX: (Called D-000177 but not currently in box 03Apr26)
		- Unapproved version: [[D-000177.pdf]]
	1. Inner piping: 1.61 in ID, 1.9 in OD - [[D-000167 1.pdf]]
		1. How long?? Is it *48.75 in long* ? 
### Heater
1. Heater: (Called D-000181 but not currently in box 03Apr26)
	1. 48.75 in long (D-000167 1)
	2. There will be trace heating 

### Loop Specs: 
Vertical height ([[D-000117a 1.pdf]]): 50 in
B_H_leg length: 49.750 in    # Modeling as 50 in % Bottom Horiz leg
T_H_leg:             49.750 in  % D-000183 rev A [[D-000183 1.pdf]]


### ~~Bends:~~ 
~~B_H_bend_length: 5.5 in each %5.593 in each~~
			~~% Bottom horizontal~~
		~~% (49 - 38.57* np.cos(10/180 * np.pi))/2 = 5.592951991200753~~
		~~- Both = 11.1859039824 in~~ 
~~T_H_bend_length = 5.5 in each % 5.408 in each~~ 
			~~% Top Horizontal~~
		~~(49/np.cos(10/180 * np.pi) - 38.94) / 2  = 5.407951991200754~~
		~~- Both = 10.815904 in~~

10° inclination  %.  np.deg2rad(10) = 0.17453 rad


- Angle of inclination still 10* from horizontal, final set of drawings pending
- Extruding pipe 4, in drawing below, is an instrument line for a TC and flowmeter type measurement, not exit volume... 