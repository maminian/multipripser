def gen_pt_cloud_from_measure(measure,npoints,*args,**kwargs):
    '''
    Generates a point cloud of npoints sampled
    from a measure function which samples from that
    measure ONCE. All *args and **kwargs are passed directly to the
    measure function.
    '''
    import numpy as np

    cloud = []
    for i in range(npoints):
        cloud.append( measure(*args,**kwargs) )
    #
    return np.array(cloud)
#
