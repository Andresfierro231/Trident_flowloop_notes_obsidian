"""Minimal pandas/JSON reader; all lengths are millimetres unless unit says deg."""
from pathlib import Path
import json
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
model=json.loads((ROOT/'data/VCU_Rev9_Engineering_Data.json').read_text())
# Pandas reads blank numeric CSV cells as NaN. JSON unknowns are None/null.
dimensions=pd.read_csv(ROOT/'data/VCU_Rev9_Dimensions.csv')
coordinates=pd.read_csv(ROOT/'data/VCU_Rev9_Coordinates.csv')
sensors=pd.read_csv(ROOT/'data/VCU_Rev9_Sensor_Stations.csv')
segments=pd.read_csv(ROOT/'data/VCU_Rev9_Segments.csv')
pipe_axes=pd.read_csv(ROOT/'data/VCU_Rev9_Pipe_Axes.csv')
diameters=pd.read_csv(ROOT/'data/VCU_Rev9_Diameters.csv')
# Ordered main-loop corner positions in the unmodified global CAD frame:
corner_order=['B','C','D','E','F','G','H','A']
corners=coordinates.set_index('id').loc[corner_order,['CAD_X_mm','CAD_Y_mm','CAD_Z_mm']]
# These are axis station markers, NOT physical sensing-junction positions:
loop_sensors=sensors[sensors['domain']=='main_loop'].copy()
station_markers=loop_sensors[['sensor_id','sensor_type','segment','station_from_start_mm','nearest_endpoint','nearest_distance_mm','projected_CAD_X_mm','projected_CAD_Y_mm','projected_CAD_Z_mm']]
if __name__=='__main__':
 print('Corners:',len(corners),'Sensor references:',len(sensors),'Numeric metrics:',len(dimensions))
 print(dimensions[dimensions['component']=='cooling_jacket'][['feature','value','unit']].to_string(index=False))
 print('Main-loop ID:',diameters.loc[diameters['item']=='Main swept loop','inner_diameter_mm'].iloc[0])
 print('Active heater length:',model['heater']['active_length_mm'])
