# Displaying results from the 2^i scaling with Cantor x [0,1].

import ripser_interface as ri
import numpy as np
from matplotlib import pyplot

results = ri.load_thing('cantor_n8192_reps100.pkl')
d = np.log(2)/np.log(3)
# d = 1
ns = np.array([result[0] for result in results])
nsu = np.unique(ns)
colors = pyplot.cm.rainbow(np.linspace(0,1,len(nsu)))
cdict = {nsuu: colors[i] for i,nsuu in enumerate(nsu)}

######################
#
# PH^0
#
fig0,ax0 = pyplot.subplots(1,1)

for result in results:
    k = len(result[1][0])-1
    if k>1:
        nv = result[0]
        birthdeath = result[1][0][:k]
        bars = np.diff(birthdeath,axis=1).flatten()
        order = np.argsort(bars)
        # ax0.step(np.linspace(0,1,k),nv**(1./d)*bars[order],c=cdict[result[0]],lw=1)
        ax0.step(np.linspace(0,1,k),bars[order],c=cdict[result[0]],lw=1)
        print(bars[order[-1]])
    #
#

for nsuu in nsu:
    ax0.plot([],[],c=cdict[nsuu],lw=2,label=r'$n=%i$'%nsuu)
#

ax0.legend(loc='upper left')
fig0.suptitle(r'$PH^0$ for the Cantor set, points sampled from $2^i$')


pyplot.show(block=False)
