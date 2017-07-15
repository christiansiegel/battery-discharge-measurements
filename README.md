Battery Discharge Measurements
------------------------------

Intended for [Electrical Circuit Battery Model](https://github.com/christiansiegel/electrical-circuit-battery-model) extraction and validation.

The following battery types are used:

* 2000 mA prismatic Li-Ion battery pack (585460)
* LR03/AAA alkaline batteries from VARTA (4103)

The measurements are performed with a 10-bit ADC. A higher resolution can be achieved by smoothing the oversampled data with, e.g. the Savitzky–Golay filter ([filter.py](filter.py)).
