import numpy as np
import time

import sys
sys.path.append("/usr/local/lib/python3.5/site-packages")
import adc001py.adc001py as adc001


"""
This is a test program which verifies that Numpy is present
and working on a system.  It works only under python3.  A 
typical run looks like this:

debian@beaglebone:~/NumpyPlaypen$ python3 test.py 
Running test 1 ...
res = 6.430323e-16
Running test 2 ...
res = 5.904837e-15
Running test 3 ...
res = 1.033523e-15
"""


def test1():
    print('Running test 1 -- matrix inverse ...')
    N = 5
    A = np.random.randn(N,N)
    Ainv = np.linalg.inv(A)
    E = np.eye(N,N)
    res = np.linalg.norm(np.matmul(A, Ainv) - E)
    print('res = %e' % res)
    print('----  Done  ----')

def test2():
    print('Running test 2 -- SVD ...')
    N = 7
    A = np.random.randn(N,N)    
    U, Sv, V = np.linalg.svd(A, full_matrices=True)
    Sm = np.zeros((N,N))
    Sm[:N, :N] = np.diag(Sv)
    A1 = np.matmul(U, np.matmul(Sm, V))
    res = np.linalg.norm(A - A1)
    print('res = %e' % res)
    print('----  Done  ----')    

def test3():
    print('Running test 3 -- dense linear solver ...')
    N = 9
    A = np.random.randn(N,N)
    x = np.random.randn(N,1)
    b = np.dot(A, x)
    x1 = np.linalg.solve(A,b)
    res = np.linalg.norm(x - x1)
    print('res = %e' % res)
    print('----  Done  ----')    

def test4():
    print('Running test 4 -- Get ID reg value from ADC-001.  ID value should be 222 ...')
    adc001.adc_config()
    adc001.adc_set_samplerate(adc001.SAMP_RATE_15625)
    adc001.adc_set_chan0()
    ID = adc001.adc_get_id_reg()
    print('ID = ',ID)
    print('----  Done  ----')    

def test5():
    print('Running test 5 -- Loop 10 times, do single ADC value and print it out ...')
    adc001.adc_config()
    adc001.adc_set_samplerate(adc001.SAMP_RATE_15625)
    adc001.adc_set_chan0()

    for i in range(10):
        volt = adc001.adc_read_single()
        print('Voltage reading = %f' % volt)
    print('----  Done  ----')    

def test6():
    print('Running test 6 -- Do multiple read of 100 values and print them out. ...')
    adc001.adc_config()
    adc001.adc_set_samplerate(adc001.SAMP_RATE_15625)
    adc001.adc_set_chan0()
    vlist = adc001.adc_read_multiple(100)
    # Create numpy vector
    v = np.array(vlist)
    print('Voltage vector =\n')
    print(v)
    # Do FFT
    vf = np.fft.fft(v)
    print('FFT =\n')
    print(vf)
    print('----  Done  ----')
    
def test7():
    """
    To do:  Fix all the magic numbers in here.
    """
    print('Running test 7 -- Loop forever, do multiple read of 1024 values, do FFT,')
    print('find peak of sig and print out corresponding freq. ...')
    adc001.adc_config()
    adc001.adc_set_samplerate(adc001.SAMP_RATE_15625)
    adc001.adc_set_chan0()

    while 1:
        v = np.array(adc001.adc_read_multiple(1024))
        # Do FFT, then compute mag of each element.
        vf = np.abs(np.fft.fft(v))
        # Look for peak, but only look in first half of spectrum
        idx = (np.where(vf == np.amax(vf[0:511])))[0][0]
        #print('idx = %d' % idx)
        if (idx == 0):
            # Just keep going if no freq is detected
            print('No frequency detected')
            continue
        # Now compute what freq this corresponds to.
        # 1024 pts, sample freq is 15625 Hz.
        fs = 15625.0
        freq = (idx/1024.0)*fs
        print('Frequency = %f' % freq)
        time.sleep(0.5)
        
    print('----  Done  ----')
    

if __name__ == "__main__":

    """
    All answers printed should be zero, within
    rounding error.
    """
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    print('================  All tests done now!  ===============')

