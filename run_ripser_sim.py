def run_ripser_sim(cloud,**kwargs):
    '''
    Purpose: Runs a ripser simulation based on the input. 
        The input can be one of two things:

        - An n-by-d array, interpreted as n points in d dimensions, 
          where the distance matrix will be built internally using 
          the two-norm as a metric.
        - An n-by-n array, which will be interpreted 
          as a distance matrix. In the rare situation that you  
          have a point cloud with the same number of points as 
          dimensionality (i.e., d=n), you may pass the optional 
          argument "cloud=True" to force the first behavior.

    Once the distance matrix is formed, a call to ripser is made,
    and the function returns a dictionary with the cleaned 
    birth/death intervals for the homology dimensions requested 
    (default: up to dimension one).

    optional arguments:
        fname: intermediate file's name. Used for running in parallel
            to prevent overlap.
        ripser_loc: string indicating location of the ripser executable.
            Defaults to a "../ripser/ripser".
        save_input: Boolean, whether to keep the distance matrix from the
            input to ripser.
            Defaults to False.
        save_output: Boolean; whether to keep the file from the calculation
            or just delete it after calculation.
            Defaults to False.
        max_dim: maximum persistent homology dimension to compute.
            Defaults to 1.
        cloud: True/False flag to override the internal logic 
            to distinguish between point cloud and distance matrix input. (default: False)
    '''
    # from create_distmat_file import create_distmat_file as cdf
    from create_distmat_str import create_distmat_str as cds
    from create_distmat import create_distmat
    from read_ripser_results import read_ripser_results as rrr
    from ripser_misc import generate_unique_id as gid

    import subprocess,os

    fgid = gid()
    fname = kwargs.get('fname',fgid+'.txt')
    ripser_loc = kwargs.get('ripser_loc','../ripser/ripser')
    save_input = kwargs.get('save_input',False)
    save_output = kwargs.get('save_output',False)
    max_dim = kwargs.get('max_dim',1)

    n,d = np.shape(cloud)
    if n==d and kwargs.get('cloud',False):
        # assume the input is a distance matrix.
        D = cloud
    else:
        D = create_distmat(cloud)
    #

    Dstr = cds(D)
    p = subprocess.Popen([ripser_loc,"--dim",str(max_dim)], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.communicate(input=Dstr)[0]

    lines = result.decode('utf-8').split('\n')
    lines.pop(-1)   # Spare extra line

    if save_output:
        f = open(fgid+'_results.txt','wb')
        f.write(result)
        f.close()

    if save_input:
        f = open(fgid+'.txt','wb')
        f.write(Dstr)
        f.close()
    #

    try:
        PH_intervals = rrr(lines)
    except:
        print('There was an error parsing the results; returning the raw result.')
        return lines
    #

    return PH_intervals
#
