# Attempting to take increasing
# sets of points sampled from cantor dust x [0,1].
#

import ripser_interface as ri
import numpy as np
from matplotlib import pyplot
import multiprocessing

fpref = ri.generate_unique_id()

def gen_cantor_pt(d=60):
    # d=40 corresponds to roughly 19 digits of precision.
    a = np.random.choice([0,2],d)
    b = 3.**np.arange(-1,-d-1,-1)
    return np.dot(a,b)
#

def gen_cantor(n,d=60):
    # points on C
    pts = np.zeros((n,1))
    pts[:,0] = [gen_cantor_pt(d=d) for i in range(n)]
    return pts
#

def PH_realization(inval):
    i,rep = inval
    fname = fpref + '_' + str(i).zfill(4) + '_' + str(rep).zfill(3) + '.txt'
    cloud = gen_cantor(i)

    PH_intervals = ri.run_ripser_sim(cloud, max_dim=0, fname=fname)
    print(i,rep)
    return i,PH_intervals
#

nproc = 60
reps = 100

p = multiprocessing.Pool(nproc)

# samples = np.arange(nmin,nmax+1,dn, dtype=int)
samples = 2**np.arange(5,13+1)
samples = np.array(samples, dtype=int)


samples = np.array([[[sample,rep] for sample in samples] for rep in np.arange(reps)])
samples = np.reshape(samples, (samples.shape[0]*samples.shape[1],2) )

results = p.map(PH_realization,samples)

ri.save_thing(results,'cantor_n%i_reps%i.pkl'%(samples.max(),reps))
