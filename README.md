## Description
Demo package for the WaveForms SDK Getting Started guide and multiple test scripts for different instruments.

Check: [Getting Started with the WaveForms SDK](https://digilent.com/reference/test-and-measurement/guides/waveforms-sdk-getting-started) for more details.

***

## Install
```
pip3 install git+https://github.com/MWMD-mfb/WaveForms-SDK-Getting-Started-PY#egg=WF_SDK
```

For Analog Discovery 3 to be detected and named correctly, add the following to _dwfconstants.py_.  
In Windows, the file is located at: `C:\Program Files (x86)\Digilent\WaveFormsSDK\samples\py\dwfconstants.py`  
In Linux, the file is located at: `/usr/share/digilent/waveforms/samples/py/dwfconstants.py`

Add the 'devidDiscovery3' line under category 'device ID':
```
# device ID
devidEExplorer   = c_int(1)
devidDiscovery   = c_int(2)
devidDiscovery2  = c_int(3)
devidDDiscovery  = c_int(4)
devidADP3X50     = c_int(6)
devidADP5250     = c_int(8)
devidDPS3340     = c_int(9)
devidDiscovery3  = c_int(10)
```

Add the 'enumfilterDiscovery3' line under category 'use deiceid':
```
#use deviceid
enumfilterEExplorer  = c_int(1)
enumfilterDiscovery  = c_int(2)
enumfilterDiscovery2 = c_int(3)
enumfilterDDiscovery = c_int(4)
enumfilterDiscovery3 = c_int(10)
```

## Available tests:
* empty test template
* analog signal generation and recording test
* digital signal generation and recording test
* blinking LEDs with the Suplpies and the Static I/O instruments
* UART in/out test using the Pmod CLS and the Pmod MAXSonar
* SPI in/out test using the Pmod CLS and the Pmod ALS
* I2C in/out test using the Pmod CLS and the Pmod TMP2
* board temperature test
* device information logging

***

## Available instruments and functions:
### Device
* open
* check_error
* close
* temperature

### Oscilloscope
* open
* measure
* trigger
* record
* close

### Waveform Generator
* generate
* close

### Power Supplies
* switch
* close

### Digital Multimeter
* open
* measure
* close

### Logic Analyzer
* open
* trigger
* record
* close

### Pattern Generator
* generate
* close

### Static I/O
* set_mode
* get_state
* set_state
* set_current - **UNTESTED**
* set_pull - **UNTESTED**
* close

### Protocol
#### UART
* open
* read
* write
* close

#### SPI
* open
* read
* write
* echange
* spy - **UNTESTED**
* close

#### I2C
* open
* read
* write
* echange
* spy - **UNTESTED**
* close
