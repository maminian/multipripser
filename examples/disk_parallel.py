# Attempting to take increasing
# sets of points sampled from circle area one.
#

import ripser_interface as ri
import numpy as np
from matplotlib import pyplot
import multiprocessing

fpref = ri.generate_unique_id()

# Want the circle to be area one.
rmax = np.sqrt(1./np.pi)

def gen_circle_pt():
    # Rejection sampling for the U(disk) distribution.
    candidate = rmax*(np.random.rand(2)*2 - 1)
    while np.linalg.norm(candidate) > rmax:
        candidate = rmax*(np.random.rand(2)*2 - 1)
    return candidate
#

def gen_circle(n):
    # points on U(circle)
    pts = np.zeros((n,2))
    for i in range(n):
        pts[i,:] = gen_circle_pt()
    return pts
#

def PH_realization(inval):
    i,rep = inval
    fname = fpref + '_' + str(i).zfill(4) + '_' + str(rep).zfill(3) + '.txt'
    cloud = gen_circle(i)

    PH_intervals = ri.run_ripser_sim(cloud, max_dim=1, fname=fname)
    print(i,rep)
    return i,PH_intervals
#

nproc = 36
nmin = 20
nmax = 5000
#dn = 20

reps = 1000

# samples = np.arange(nmin,nmax+1,dn, dtype=int)
coeffs = np.arange(1,10,0.5)
powers = 10.**np.arange(4)
nc = len(coeffs)
npow = len(powers)
coeffs.shape = (nc,1)
powers.shape = (1,npow)
samples = np.dot(coeffs,powers).flatten()
samples = samples[samples>=nmin]
samples = samples[samples<=nmax]

samples = np.array(samples, dtype=int)
print(samples)
print(len(samples))

p = multiprocessing.Pool(nproc)

samples = np.array([[[sample,rep] for sample in samples] for rep in np.arange(reps)])
samples = np.reshape(samples, (samples.shape[0]*samples.shape[1],2) )

print(len(samples))

results = p.map(PH_realization,samples)

ri.save_thing(results,'circle_n%i_reps%i.pkl'%(nmax,reps))
