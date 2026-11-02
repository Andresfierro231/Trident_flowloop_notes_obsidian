
### Definitions
* An “experiment” is a steady-state condition with a fixed heater power and known ambient temperature, with measured temperatures at 18 locations (PTC 1-6 and STC 1-12).
* The **forward** problem is:
	- given the data (thermal resistances between all nodes) 
	- Given the input (ambient temp and heater power)
	- compute the temperature at all measured locations for the experiment.
* The **inverse** problem is:
	- The data from one experiment is: temperature at PTC 1-6 and STC 1-12, heater power, and ambient temp.
	- Given: data from many experiments
	- Calibrate the thermal resistances between all nodes
If:
- There is no flow, the thermal conductivity is not dependent on temperature, and if there is no radiative/convective heat transfer from the insulation to the environment,
	- then the problem is linear (?? Would it not depend on the property dependence on T?)

### Assumptions
The assumptions:
- If you start with a reasonable thermal resistance, the calibration (inverse problem) will be much easier.
	- So if you have (approximate) details on material properties, its not bad to include it in the thermal resistance and only calibrate a “correction” to that.
- If you start calibrating with the assumption that it is linear, 
	- Then the calibration will be easy and require little data
- Then if you allow for non-linearity, it will only tweak the linear solution to pick up the small nonlinearities much easier.

After you get this working and we can compare with some of their data - maybe even provide some predictions, then we can work on the time-dependent ones that Nick proposed, which will add calibration of the heat capacities.


[[TACC Background Process Diagnostics and Cleanup]] 

