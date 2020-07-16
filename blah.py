import numpy as np
import l_systems as ls
import ripser_interface as ri
import test_measures as tm
from matplotlib import pyplot
from sklearn import metrics

mu4 = ls.sierpinski.drawcurve(ls.sierpinski.l_iters(4), rescale=True)

pyplot.ion()

fig,ax = pyplot.subplots(1,1)
ax.plot(mu4[:,0], mu4[:,1])
ax.axis('square')
fig.show()

coll = np.array([tm.sample_piecewise(mu4) for _ in range(100)])
ax.scatter(coll[:,0], coll[:,1], c=['r'], s=20)

fig2,ax2 = pyplot.subplots(1,1)

nsamp = 10000
coll = np.array([tm.sample_piecewise(mu4) for _ in range(nsamp)])

D_mu4 = metrics.pairwise_distances(mu4) # pairwise distances between vertices on measure.
D = metrics.pairwise_distances(coll)    # pairwise distances of random sampling of measure.
D_vert = metrics.pairwise_distances(coll,mu4)   # pairwise distances between prior two.

Dtil = np.array(D)  # Distances when replacing randomly sampled points with nearest vertex.
for i in range(nsamp):
    nni = np.argmin(D_vert[i])
    for j in range(i):
        nnj = np.argmin(D_vert[j])
        Dtil[i,j] = D_mu4[nni,nnj]
        Dtil[j,i] = D_mu4[nni,nnj]
    #
    if i%(nsamp//10)==0:
        print(i,nsamp)
#

# Error in distance matrix
E = Dtil - D
errs = E.flatten()
errs = errs[errs!=0.]    # Don't care about the diagonal
eps = np.linalg.norm(mu4[1]-mu4[0]);

# Visualize distribution of errors
ax2.hist(errs, bins=np.linspace(-eps,eps,41))
fig2.show()
