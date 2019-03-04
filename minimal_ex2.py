import numpy as np
import ripser_interface as ri
from sklearn import metrics
th = np.linspace(0,2*np.pi,201)
x = np.cos(th) + 0.1*np.random.randn(201)
y = np.sin(th) + 0.1*np.random.randn(201)
cloud = np.vstack([x,y]).T
D = metrics.pairwise_distances(cloud, metric='cosine')
result = ri.run_ripser_sim(D)
fig,ax = ri.plot_PH_summary(result)
