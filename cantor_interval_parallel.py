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

def gen_cantor_cross_interval(n,d=60):
    # points on C x U([0,1])
    pts = np.zeros((n,2))
    pts[:,0] = [gen_cantor_pt(d=d) for i in range(n)]
    pts[:,1] = np.random.rand(n)
    return pts
#

def PH_realization(inval):
    i,rep = inval
    fname = fpref + '_' + str(i).zfill(4) + '_' + str(rep).zfill(3) + '.txt'
    cloud = gen_cantor_cross_interval(i)

    PH_intervals = ri.run_ripser_sim(cloud, max_dim=1, fname=fname)
    print(i,rep)
    return i,PH_intervals
#

nproc = 4
nmin = 20
nmax = 200
dn = 20

reps = 100

p = multiprocessing.Pool(nproc)

samples = np.arange(nmin,nmax+1,dn, dtype=int)
samples = np.array([[[sample,rep] for sample in samples] for rep in np.arange(reps)])
samples = np.reshape(samples, (samples.shape[0]*samples.shape[1],2) )

results = p.map(PH_realization,samples)

ri.save_thing(results,'cantor_interval_n%i_reps%i.pkl'%(nmax,reps))
