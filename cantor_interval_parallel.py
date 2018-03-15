# Attempting to take increasing
# sets of points sampled from cantor dust x [0,1].
#

import ripser_interface as ri
import numpy as np
from matplotlib import pyplot
import multiprocessing

fpref = ri.generate_unique_id()

def PH_realization(inval):
    i,rep = inval
    fname = fpref + '_' + str(i).zfill(4) + '_' + str(rep).zfill(3) + '.txt'
    cloud = ri.gen_pt_cloud_from_measure(ri.test_measures.cantor_cross_interval,i)

    PH_intervals = ri.run_ripser_sim(cloud, max_dim=1, fname=fname)
    print(i,rep)
    return i,PH_intervals
#

nproc = 60
nmin = 20
nmax = 1000
#dn = 20

reps = 100

# samples = np.arange(nmin,nmax+1,dn, dtype=int)
# coeffs = np.arange(1,10,0.5)
# powers = 10.**np.arange(4)
#nc = len(coeffs)
#npow = len(powers)
#coeffs.shape = (nc,1)
#powers.shape = (1,npow)
#samples = np.dot(coeffs,powers).flatten()
#samples = samples[samples>=nmin]
#samples = samples[samples<=nmax]

samples = 2**np.arange(5,13+1)

samples = np.array(samples, dtype=int)
print(samples)
print(len(samples))

p = multiprocessing.Pool(nproc)

samples = np.arange(nmin,nmax+1,dn, dtype=int)

samples = np.array([[[sample,rep] for sample in samples] for rep in np.arange(reps)])
samples = np.reshape(samples, (samples.shape[0]*samples.shape[1],2) )

print(len(samples))

results = p.map(PH_realization,samples)

#ri.save_thing(results,'cantor_interval_n%i_reps%i.pkl'%(nmax,reps))
ri.save_thing(results,'cantor_interval_n%i_reps%i_2pow.pkl'%(np.array(samples).max(),reps))
