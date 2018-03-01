
def create_distmat(cloud):
    '''
    Create distance matrix. outputs np array.
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
    D = sklearn.metrics.pairwise.pairwise_distances(cloud)
    return D
#
