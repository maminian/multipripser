# Attempting to take increasing
# sets of points sampled from [-1,1]x[-1,1]
# and parallelize the calculation of *average edge length*
# for PH^0.
#

import ripser_interface as ri
import numpy as np
from matplotlib import pyplot
import multiprocessing

n = 1001
pts = np.random.rand(n,2)*2 - 1.

def PH_realization(i):
    cloud = pts[:i]
    PH_intervals = ri.run_ripser_sim(cloud, max_dim=0)
    print(i)
    return PH_intervals
#

p = multiprocessing.Pool(4)

results = p.map(PH_realization,np.arange(2,n, dtype=int))

ri.save_thing(results,'square_1000.pkl')
