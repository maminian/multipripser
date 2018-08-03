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

def plot_PH_results(arr,**kwargs):
    '''
    Makes the traditional PH plot using the given
    array of birth/death times (n-by-2).

    Returns a fig,ax pair and does a pyplot.show(block=False).

    optional arguments:
        plot_infinite_bar: True by default.
            Whether to plot the half-infinite bars.
            This is hacky - it just plots beyond the
            range of the plot that would exist without it.
        xrange: list of floats [xl,xr],
            of the desired bounds for the barcode.
            Useful in conjunction with plot_infinite_bar
            to ensure that you get the desired
            window while making the infinite bars still
            seem infinite. Default: empty list; automatically determined.
        yrange: list of floats [yl,yr],
            for the plotting window. Desirable if you want
            to fix the height of the bars.
    '''
    import numpy as np
    from matplotlib import pyplot
    from matplotlib import patches

    filt_range = kwargs.get('filt_range', [])

    n = len(arr)

    if len(kwargs.get('yrange',[]))>0:
        yl,yr = kwargs.get('yrange')
    else:
        yl,yr = 0.,1.
    #

    dh = (yr-yl)/n
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
    if len(kwargs.get('xrange',[]))>0:
        xl,xr = kwargs.get('xrange')
    else:
        xl = 0
        xr = arr[inds,1].max()*1.05
    #

    # intervals with infinity get treated separately
    # after the main plot so that they show up in the same
    # plot. This is a little hacky.

    if kwargs.get('plot_infinite_bar', True):
        for thing in dolater:
            i,(l,r) = thing
            r_repl = xr+1
            rw = r_repl - l
            ax.add_patch(patches.Rectangle( (l,i*dh), rw, rh ))
    #

    ax.set_xlim([xl,xr])

    pyplot.show(block=False)
    return fig,ax
#

def plot_PH_summary(PH_dict,**kwargs):
    '''
    Constructs a pretty version of barcodes of all available
    dimensions in an n-by-1 plot, which has a single
    horizontal axis of filtration values.

    Optional inputs:
        max_dim : maximum homologogical dimension to bother with.
            Default: all in the dictionary are used.
    '''
    import numpy as np
    from matplotlib import pyplot
    from matplotlib import patches
    import pdb

    dims = np.array(list(PH_dict.keys()))
    keeps = np.where(dims <= kwargs.get('max_dim',np.inf))[0]
    dims = dims[keeps]
    dims.sort()

    ndims = len(dims)
    # NOTE: code will break with more than 10 dimensions.
    colors = pyplot.cm.tab10(np.linspace(0,1,10))

    xl = 0.
    xr = 1.1*max([np.nanmax(PH_dict[d][np.isfinite(PH_dict[d])]) for d in [0,1]])


    fig,ax = pyplot.subplots(ndims,1, sharex=True, figsize=(12,2*ndims))


    for j,d in enumerate(dims):
        # filt_range = kwargs.get('filt_range', [])
        arr = PH_dict[d]
        n = len(arr)

        dh = 0.1
        r = 0.3 # Relative padding between consecutive intervals

        rh = dh-r*dh

        dolater = []

        for i,interval in enumerate(arr):
            l,r = interval
            if r == np.inf:
                dolater.append([i,interval])
            else:
                rw = r-l
                # Rectangular patches are given as (left,bottom), width, height.j
                ax[j].add_patch(patches.Rectangle( (l,i*dh), rw, rh, color=colors[j]))
            #
        #

        inds = np.isfinite(arr[:,1])
        xl = 0.

        # intervals with infinity get treated separately
        # after the main plot so that they show up in the same
        # plot. This is a little hacky.


        for thing in dolater:
            i,(l,r) = thing
            r_repl = xr+1
            rw = r_repl - l
            ax[j].add_patch(patches.Rectangle( (l,i*dh), rw, rh, color=colors[j]) )
        #

        ax[j].set_xlim([xl,xr])
        ax[j].set_ylim([0,len(arr)*dh])
    #

    for axi in ax:
        axi.set_yticks([])
        for po in ['right','top','left']:
            axi.spines[po].set_visible(False)
    #

    # Keep this - it cleans up space horizontally as well.
    fig.tight_layout()

    # We're manually resizing the vertical real estate
    # of the axes here to account for padding,
    # and giving spaces for some text.
    bottom_pad = 0.1   # note: units relative to total figure height 1.
    inter_pad = 0.12
    top_pad = 0.1
    remainder = 1. - bottom_pad - top_pad - inter_pad*(ndims-1)

    barcounts = [len(PH_dict[d]) for d in dims]
    new_heights = np.array(barcounts)/np.sum(barcounts)*remainder

    ypos = 1. - top_pad
    for i in range(len(ax)):
        bbox = ax[i].get_position()

        # left, bottom, width, height
        bot = ypos - new_heights[i]

        newbbox = [bbox.x0, bot, bbox.width, new_heights[i]]

        ax[i].set_position(newbbox)
        ypos -= new_heights[i] + inter_pad
    #

    # Put in labels for each barcode.
    for i,d in enumerate(dims):
        ax[i].text(0,1, 'Persistence intervals in dimension %i:'%d, ha='left', va='bottom', fontsize=14, transform=ax[i].transAxes)
    #

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

def export_results_to_hdf(results,fname):
    '''
    Dumps the results of a many-realization results into an
    HDF file which can be read by both python and matlab.
    '''
    import h5py
    import numpy as np

    h = h5py.File(fname,'w')
    ns = np.array([result[0] for result in results])
    nsu = np.unique(ns)

    phs = []
    for result in results:
        vals = list(result[1].keys())
        for val in vals:
            if val not in phs:
                phs.append(val)
    #
    for ph in phs:
        h.create_group('/PH_%i'%ph)
    #

    counter = np.zeros(ns.shape)
    for i,result in enumerate(results):
        nsuu = result[0]
        which = np.where(nsuu==nsu)[0][0]
        bddict = result[1]
        phs = list(bddict.keys())
        for j,ph in enumerate(phs):
            dsetname = '/PH_%i/n%i_%i'%(ph,nsuu,counter[which])
            print(dsetname)
            h.create_dataset(dsetname, data=bddict[ph])
            counter[which]+=1
        #
    #
#
