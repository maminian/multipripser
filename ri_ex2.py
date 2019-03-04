# Example 2: a "barrel" in three dimensions.
# Basically a noisy hollow sphere with the top removed.
#
# We do a lot more fancy stuff here in the visualization.
#

import ripser_interface as ri
import numpy as np
from matplotlib import pyplot

# for 3d scatter plot
from mpl_toolkits.mplot3d import Axes3D

# fast distance matrix
from sklearn import metrics

######################
#
# make the cloud of points
#

n = 201
t = np.linspace(0,2*np.pi,n)
cloud = np.zeros((n,3))

# Make a cloud of points in a barrel; the 
# spherical polar coordinate is cut off from below.
phi_min = np.pi/3
phi_max = np.pi - phi_min

for i,tv in enumerate(t):
    phi = phi_min + (phi_max - phi_min)*np.random.rand()
    cloud[i] = [np.cos(tv)*np.sin(phi),np.sin(tv)*np.sin(phi), np.cos(phi) ]
    cloud[i] += 0.02*np.random.randn(3)
#

######################
#
# main calculation of persistence intervals via ripser
#

PH_intervals = ri.run_ripser_sim(cloud, max_dim=2)

fig,ax = ri.plot_PH_summary(PH_intervals, show=False)

######################
#
# let's get fancy: plot the point cloud in three dimensions on the left
# with some extra doodads.
#

# Apologies; subplots_adjust seems to tamper with the y-positioning
# of the axes of the existing plots even if only the "left" argument is
# specified.
for axt in ax:
    bbox_t = axt.get_position()
    axt.set_position([bbox_t.x0 + bbox_t.width/2. +0.01, bbox_t.y0, bbox_t.width/2. - 0.02, bbox_t.height])
#

axl = fig.add_axes([0.02,0.02,0.46,0.96], projection='3d')

axl.scatter(cloud[:,0], cloud[:,1], cloud[:,2], c='k', s=10)

# Look at the connected graph somewhere in the interval of the  
# largest 1-dimensional hole.
max_1d_idx = np.argmax( np.diff( PH_intervals[1], axis=1 ) )
birth,death = PH_intervals[1][max_1d_idx]

epsilon = birth # certainly could choose other points in this interval

D = metrics.pairwise_distances(cloud, metric='euclidean')

# Collect the neighbor information associated 
# with this value of epsilon, to be usd for plotting.
locs = np.where(D <= epsilon)
indices = [ locs[1][ np.where(locs[0]==row)[0] ]  for row in np.unique(locs[0]) ]

for j,row in enumerate(indices):
    eh = np.setdiff1d(row, [j])
    for idx in eh:
        vec = cloud[ [j,idx] ]
        axl.plot(vec[:,0], vec[:,1], vec[:,2], c='r', lw=0.5, alpha=0.4)
#

# Setting the axis view and saving...
axl.set_xlim([-1,1])
axl.set_ylim([-1,1])
axl.set_zlim([-1,1])

axl.view_init(elev=45.)

fig.show()
#fig.savefig('ri_ex2_figure.png', dpi=120, bbox_inches='tight')

