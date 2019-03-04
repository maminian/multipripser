import ripser_interface as ri
import numpy as np
from matplotlib import pyplot

n = 101
th = np.linspace(0, 2*np.pi, n)
x = np.cos(th) + 0.1*np.random.randn(n)
y = np.sin(th) + 0.1*np.random.randn(n)
cloud = np.vstack( [x,y] ).T

# Look at the points themselves
fig2,ax2 = pyplot.subplots(1,1)
ax2.scatter(x,y, c='k')
ax2.axis('equal')
fig2.show()

# Find the barcodes
results = ri.run_ripser_sim(cloud)
fig,ax = ri.plot_PH_summary(results)

