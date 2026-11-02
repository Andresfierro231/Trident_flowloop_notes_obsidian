Based on Gentry's [[MainVault/Box/VCU ACU Shared Research/Design_Documentation/Drawings/ACU STNCL Loop Drawings/3D Models/ExtractedMeasurements.txt|ExtractedMeasurements]]

Back: [[Trident - STNCL Loops]]

> Loop position is the distance along the loop axis, beginning at the middle of the `DOWN_BOTTOM` bend. All positions and lengths are in centimeters unless otherwise stated.

## General Specifications

| Parameter           |    Value | Unit | Implem  |
| ------------------- | -------: | ---- | ------- |
| Fluid material      | `hitech` | —    | EOS     |
| Pipe material       |  `ss316` | —    | ss-mat  |
| Pipe inner radius   |    1.330 | cm   | pipe_ID |
| Pipe outer radius   |    1.670 | cm   | pipe_OD |
| Pipe wall thickness |    0.340 | cm   |         |
| Total loop length   |  568.744 | cm   |         |

## Bend Geometry

| Bend          | Inner length (cm) | Bend angle (°) | Calculated radius (cm) | Calculated arc length (cm) |
| ------------- | ----------------: | -------------: | ---------------------: | -------------------------: |
| `DOWN_BOTTOM` |            11.410 |         82.420 |                  8.370 |                     12.040 |
| `BOTTOM_UP`   |             9.560 |         97.610 |                  8.318 |                     14.171 |
| `UP_TOP`      |            11.320 |         82.390 |                  8.315 |                     11.956 |
| `TOP_DOWN`    |             9.640 |         97.580 |                  8.371 |                     14.257 |

## Leg Geometry and Positions

| Leg      | Starting bend | Ending bend   | Inclination (°) | Initial half-bend (cm) | Flat length (cm) | Final half-bend (cm) | Total length (cm) | Leg start (cm) | Flat start (cm) | Flat end (cm) | Leg end (cm) |
| -------- | ------------- | ------------- | --------------: | ---------------------: | ---------------: | -------------------: | ----------------: | -------------: | --------------: | ------------: | -----------: |
| `BOTTOM` | `DOWN_BOTTOM` | `BOTTOM_UP`   |           7.580 |                  6.020 |          131.290 |                7.086 |           144.395 |          0.000 |           6.020 |       137.310 |      144.395 |
| `UP`     | `BOTTOM_UP`   | `UP_TOP`      |      -0.030 # 0 |                  7.086 |          126.890 |                5.978 |           139.954 |        144.395 |         151.481 |       278.371 |      284.349 |
| `TOP`    | `UP_TOP`      | `TOP_DOWN`    |           7.580 |                  5.978 |          131.370 |                7.129 |           144.477 |        284.349 |         290.327 |       421.697 |      428.826 |
| `DOWN`   | `TOP_DOWN`    | `DOWN_BOTTOM` |           0.000 |                  7.129 |          126.770 |                6.020 |           139.918 |        428.826 |         435.955 |       562.725 |      568.744 |

## Cooling Jacket

| Parameter                               |   Value | Unit |
| --------------------------------------- | ------: | ---- |
| Cooling-jacket inner radius             |   7.460 | cm   |
| Cooling-jacket length                   | 101.600 | cm   |
| Cooling-jacket start position           | 311.847 | cm   |
| Cooling-jacket end position             | 413.447 | cm   |
| Offset from start of `TOP` flat section |  21.520 | cm   |

## Luna Fibers

| Fiber | Leg | Offset from flat start (cm) | Loop position (cm) | Measured angle (°) | Converted angle (°) |
|---|---|---:|---:|---:|---:|
| LF-1 | `BOTTOM` | 130.060 | 136.080 | 0.000 | 90.000 |
| LF-2 | `UP` | 114.190 | 265.671 | 0.000 | 90.000 |
| LF-3 | `TOP` | 128.930 | 419.257 | 0.000 | 270.000 |
| LF-4 | `DOWN` | 114.070 | 550.025 | 0.000 | 270.000 |

## Wall Thermocouples

> Wall thermocouple length extends in the positive flow direction.

| Thermocouple | Leg      | Offset from flat start (cm) | Loop position (cm) | Measured angle (°) | Converted angle (°) | Length (cm) |
| ------------ | -------- | --------------------------: | -----------------: | -----------------: | ------------------: | ----------: |
| WTC-1        | `BOTTOM` |                     118.960 |            124.980 |            -90.000 |               0.000 |       3.500 |
| WTC-2        | `UP`     |                      29.010 |            180.491 |            -90.000 |               0.000 |       3.500 |
| WTC-3        | `UP`     |                     108.390 |            259.871 |            -90.000 |               0.000 |       3.500 |
| WTC-4        | `TOP`    |                      20.900 |            311.227 |            -90.000 |               0.000 |       3.500 |
| WTC-5        | `TOP`    |                     120.240 |            410.567 |            -90.000 |               0.000 |       3.500 |
| WTC-6        | `DOWN`   |                      15.600 |            451.555 |            -90.000 |               0.000 |       3.500 |
| WTC-7        | `DOWN`   |                      74.660 |            510.615 |            -90.000 |               0.000 |       3.500 |

## Penetrating Thermocouples

| Thermocouple | Leg | Offset from flat start (cm) | Loop position (cm) | Measured angle (°) | Converted angle (°) | Penetration length (cm) |
|---|---|---:|---:|---:|---:|---:|
| PTC-1 | `BOTTOM` | 1.710 | 7.730 | 30.000 | 120.000 | 0.860 |
| PTC-2 | `BOTTOM` | 130.020 | 136.040 | 30.000 | 120.000 | 0.910 |
| PTC-3 | `TOP` | 15.800 | 306.127 | 30.000 | 240.000 | 0.910 |
| PTC-4 | `TOP` | 128.830 | 419.157 | 30.000 | 240.000 | 1.550 |

## Heating Tape

| Parameter | Value | Unit |
|---|---:|---|
| Offset from start of `BOTTOM` flat section | 4.290 | cm |
| Heating-tape start position | 10.310 | cm |
| Heating-tape length | 123.830 | cm |
| Heating-tape end position | 134.140 | cm |

## Angle Conversion

| Leg              | Conversion                                                          |
| ---------------- | ------------------------------------------------------------------- |
| `BOTTOM` or `UP` | $\theta_{\mathrm{converted}}=90^\circ+\theta_{\mathrm{measured}}$   |
| `TOP` or `DOWN`  | $\theta_{\mathrm{converted}}=270^\circ-\theta_{\mathrm{measured}}$  |
| Any leg          | A result numerically equal to $360^\circ$ is converted to $0^\circ$ |


