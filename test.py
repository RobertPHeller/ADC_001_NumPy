import adc001py
from adc001py import *
adc_config()
adc_set_samplerate(SAMP_RATE_31250)
adc_set_chan0()
volts = adc_read_multiple(64)
print(volts)
adc_quit()

