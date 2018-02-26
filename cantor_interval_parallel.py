# Attempting to take increasing
# sets of points sampled from cantor dust x [0,1].
#

import ripser_interface as ri
import numpy as np
from matplotlib import pyplot
import multiprocessing

def gen_cantor_pt(d=40):
    # d=40 corresponds to roughly 19 digits of precision.
    a = np.random.choice([0,2],d)
    b = 3.**np.arange(-1,-d-1,-1)
    return np.dot(a,b)
#

n = 1001
pts = np.zeros((n,2))
pts[:,0] = [gen_cantor_pt() for i in range(n)]
pts[:,1] = np.random.rand(n)

def PH_realization(i):
    cloud = pts[:i]
    PH_intervals = ri.run_ripser_sim(cloud, max_dim=1)
    print(i)
    return PH_intervals
#

p = multiprocessing.Pool(4)

results = p.map(PH_realization,np.arange(2,n, dtype=int))

ri.save_thing(results,'cantor_interval_1000.pkl')
