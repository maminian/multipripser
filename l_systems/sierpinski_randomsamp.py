from . import sierpinski as sp
import numpy as np
from matplotlib import pyplot

cstr = sp.l_iters(10)
c = sp.drawcurve(cstr,rescale=True)

n = 1000
rs = np.random.choice(len(c)-1,n)
ts = (len(c)-1)*np.random.rand(n)
pts = np.zeros((n,2))

for i,tv in enumerate(ts):
    r = int(tv)
    t = tv-r
    pts[i] = (c[r] + t*(c[r+1]-c[r]))

fig,ax = pyplot.subplots(1,1)
ax.plot(c[:,0],c[:,1],c='k',zorder=-1000)
ax.scatter(pts[:,0],pts[:,1],c='r',s=2,zorder=1000)

pyplot.show(block=False)
