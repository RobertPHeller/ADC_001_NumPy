import numpy as np
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

def test3():
    print('Running test 3 -- dense linear solver ...')
    N = 9
    A = np.random.randn(N,N)
    x = np.random.randn(N,1)
    b = np.dot(A, x)
    x1 = np.linalg.solve(A,b)
    res = np.linalg.norm(x - x1)
    print('res = %e' % res)

def test4():
    adc001.adc_config()
    adc001.adc_set_samplerate(adc001.SAMP_RATE_15625)
    adc001.adc_set_chan0()
    ID = adc001.adc_get_id_reg()
    print('ID = ',ID)


if __name__ == "__main__":
    """
    All answers printed should be zero, within
    rounding error.
    """
    test1()
    test2()
    test3()
    test4()
    print('All done now!')

