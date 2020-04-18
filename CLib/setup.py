from distutils.core import setup, Extension

setup(name="adc001py",
      version="1.0",
      py_modules=['adc001py'],
      ext_modules = [
        Extension("_adc001py",
                  ["adc001py.i","adcdriver_host.c",
                  "prussdrv.c","spidriver_host.c"],
                  include_dirs = [".", "../PRU"])
        ]
      )
                  
