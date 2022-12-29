
def create_distmat(cloud, *args, **kwargs):
    '''
    Create distance matrix. outputs np array.
    Just an interface to sklearn.metrics.pairwise_distances; 
    args and kwargs are passed along directly.
    '''
    # import numpy as np
    import sklearn.metrics

    # n = len(cloud)
    # D = np.zeros((n,n))
    #
    # for i in range(n):
    #     for j in range(i):
    #         D[i,j] = np.linalg.norm(cloud[i]-cloud[j])
    # #
    D = sklearn.metrics.pairwise.pairwise_distances(cloud, *args, **kwargs)
    return D
#
