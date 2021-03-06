import ripser_interface as ri
import pickle
import numpy as np

#################################
#
# Parameters
#
nprocs = 1
# npoints = 8192
# seq = np.arange(20,npoints+1,20)
seq = np.array( 1.5**np.arange(8,24), dtype=int)
# seq = np.array( 1.5**np.arange(8,20), dtype=int)
npoints = seq.max()

# Generate the curve approximating sierpinski
# at a given scale. Use even numbers.
level = 6

#############################################

cstr = ri.l_systems.sierpinski.l_iters(level)
c = ri.l_systems.sierpinski.drawcurve(cstr, rescale=True)

def s_measure():
    return ri.test_measures.sample_piecewise(c)
#

results = ri.single_sequence_scaling(s_measure, npoints, seq=seq, nprocs=nprocs)

f = open('sierpinski_lvl%i_n%i.pkl'%(level,npoints),'wb')
pickle.dump(results,f)
f.close()
