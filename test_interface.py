# Actually working with ripser with our shitty interface.


import ripser_interface as ri
import numpy as np
from matplotlib import pyplot

n = 1001
t = np.linspace(0,2*np.pi,n, endpoint=False)
cloud = np.zeros((n,3))

for i,tv in enumerate(t):
    cloud[i] = [np.cos(tv),np.sin(tv),np.sqrt(2.)/3.*np.cos(3*tv)]
    cloud[i] += 0.2*np.random.randn(3)
#

PH_intervals = ri.run_ripser_sim(cloud)

fig0,ax0 = ri.plot_PH_results(PH_intervals[0])
fig1,ax1 = ri.plot_PH_results(PH_intervals[1])
