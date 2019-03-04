# Actually working with ripser with our shitty interface.


import ripser_interface as ri
import numpy as np
from matplotlib import pyplot

n = 201
t = np.linspace(0,2*np.pi,n)
cloud = np.zeros((n,3))

# Make a cloud of points in a "barrel"; spherical polar coordinate 
# restricted to the equator region.
for i,tv in enumerate(t):
    phi = np.pi/4 + np.pi/2*np.random.rand()
    cloud[i] = [np.cos(tv)*np.sin(phi),np.sin(tv)*np.sin(phi), np.cos(phi) ]
    cloud[i] += 0.05*np.random.randn(3)
#

PH_intervals = ri.run_ripser_sim(cloud, max_dim=2)

#fig0,ax0 = ri.plot_PH_results(PH_intervals[0])
#fig1,ax1 = ri.plot_PH_results(PH_intervals[1])

fig,ax = ri.plot_PH_summary(PH_intervals)
