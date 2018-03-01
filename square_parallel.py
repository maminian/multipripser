# Attempting to take increasing
# sets of points sampled from [-1,1]x[-1,1]
# and parallelize the calculation of *average edge length*
# for PH^0.
#

import ripser_interface as ri
import numpy as np
from matplotlib import pyplot
import multiprocessing

n = 8192

def PH_realization(i):
    cloud = np.random.rand(n,2)
    PH_intervals = ri.run_ripser_sim(cloud, max_dim=0)
    print(i)
    return PH_intervals
#

p = multiprocessing.Pool(4)

samples = 2**np.arange(5,13+1)
reps = 100

samples = np.array([[[sample,rep] for sample in samples] for rep in np.arange(reps)])
samples = np.reshape(samples, (samples.shape[0]*samples.shape[1],2) )

results = p.map(PH_realization,samples)

ri.save_thing(results,'square_n%i_reps%i.pkl'%(samples.max(),reps))
