# Actually working with ripser with our shitty interface.


import ripser_interface as ri
import numpy as np
from matplotlib import pyplot
import multiprocessing

fpref = ri.generate_unique_id()

n = 1001
t = np.linspace(0, 2*np.pi, n, endpoint=False)
rawcurve = np.zeros((n,3))
for i,tv in enumerate(t):
    rawcurve[i] = [np.cos(tv),np.sin(tv),np.sqrt(2.)/3.*np.cos(3*tv)]
#


def PH_realization(inv):
    fname = fpref + '_' + str(inv).zfill(4) + '.txt'
    cloud = np.zeros((n,3))
    cloud = rawcurve + 0.2*np.random.randn(rawcurve.shape[0],rawcurve.shape[1])
    PH_intervals = ri.run_ripser_sim(cloud,fname=fname)
    print(inv)
    return PH_intervals
#

p = multiprocessing.Pool(12)

results = p.map(PH_realization,[i for i in range(24)])
