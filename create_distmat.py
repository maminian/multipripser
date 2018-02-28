
def create_distmat(cloud):
    '''
    Create distance matrix. outputs np array.
    '''
    import numpy as np

    n = len(cloud)
    D = np.zeros((n,n))

    for i in range(n):
        for j in range(i):
            D[i,j] = np.linalg.norm(cloud[i]-cloud[j])
    #
    return D
#
