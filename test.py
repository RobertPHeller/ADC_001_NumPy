import sys
sys.path.append("/usr/local/lib/python3.5/site-packages")
import adc001py
from adc001py import *
adc001py.adc_config()
adc001py.adc_set_samplerate(adc001py.SAMP_RATE_31250)
adc001py.adc_set_chan0()
volts = adc001py.adc_read_multiple(64)
print(volts)
adc001py.adc_quit()

