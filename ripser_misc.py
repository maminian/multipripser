from numpy import random
import time
def generate_unique_id():
    '''
    Makes a "unique" id, to be used for filenames to avoid overlap with
    parallel computation.
    '''
    prefix = str(time.mktime(time.localtime())+time.clock())
    suffix = '_'+str(random.randint(100))
    out = prefix+suffix
    return ''.join(str(out).split('.')) # Removes decimal points
#


def plot_PH_results(arr):
    '''
    Makes the traditional PH plot using the given
    array of birth/death times (n-by-2).

    Returns a fig,ax pair and does a pyplot.show(block=False).
    '''
    import numpy as np
    from matplotlib import pyplot
    from matplotlib import patches
    n = len(arr)
    dh = 1./(n)
    r = 0.1 # Relative padding between consecutive intervals

    rh = dh-r*dh
    fig,ax = pyplot.subplots(1,1)

    dolater = []

    for i,interval in enumerate(arr):
        l,r = interval
        if r == np.inf:
            dolater.append([i,interval])
        else:
            rw = r-l
            # Rectangular patches are given as (left,bottom), width, height.j
            # print((l,i*dh), rw, rh)
            ax.add_patch(patches.Rectangle( (l,i*dh), rw, rh ))
        #
    #

    inds = np.isfinite(arr[:,1])
    ax.set_xlim([0,arr[inds,1].max()*1.05])

    pyplot.show(block=False)
    return fig,ax
#

def sum_PH_bars(PH_dict,dim=0):
    '''
    Returns the ``definite integral" of the barcode; the sum of
    the lengths of each interval in the dictionary with the assumption
    that they're arranged in [0,1]. Equivalent to taking the average.
    Throws out infinite lengths.
    '''
    import numpy as np
    lens = np.diff(PH_dict[dim]).flatten()
    return np.sum(lens[np.isfinite(lens)])
#

def save_thing(thing,fname):
    '''
    automates calling pickle.dump.
    '''
    import pickle
    f = open(fname,'wb')
    pickle.dump(thing,f)
    f.close()
    return
#

def load_thing(fname):
    '''
    automates calling pickle.load.
    '''
    import pickle
    f = open(fname,'rb')
    thing = pickle.load(f)
    f.close()
    return thing
#
