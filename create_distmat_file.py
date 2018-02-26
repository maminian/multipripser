def create_distmat_file(cloud,fname,return_mat=True):
    '''
    Given a point cloud (numpy array)
    compute the point cloud and export to file.
    '''
    import numpy as np

    n = len(cloud)
    if return_mat:
        D = np.zeros((n,n))

    f = open(fname,'w')
    # f.write('\n')   #First line blank

    for i in range(n):
        line = ''
        for j in range(i):
            val = np.linalg.norm(cloud[i]-cloud[j])
            line += '%.15f,'%val
            if return_mat:
                D[i,j] = val
            #
        #
        line += '\n'
        f.write(line)
    #
    f.close()

    if return_mat:
        return D
    else:
        return
    #
#

if __name__=="__main__":
    # Try an example with the hypothesized 3D
    # MDS embedding of the circle.
    import numpy as np
    from matplotlib import pyplot

    n = 31
    t = np.linspace(0,2*np.pi,n, endpoint=False)
    cloud = np.zeros((n,3))

    for i,tv in enumerate(t):
        cloud[i] = [np.cos(tv),np.sin(tv),np.sqrt(2.)/3.*np.cos(3*tv)]
    #
    D = create_distmat_file(cloud,'test.txt')

    pyplot.contourf(D+D.T)
    pyplot.show(block=False)
#
