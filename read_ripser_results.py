def read_ripser_results(fname):
    '''
    Purpose: reads the raw output of ripser and returns
        a dictionary with the results in a useable format.

    Inputs:
        fname : Can be either a string indicating a file on disk 
            containing the output of a ripser call,
            or a list of strings containing the lines from reading a ripser call.

    Outputs:
        PH_intervals : A dictionary whose keys are homological 
            dimensions and corresponding entries are numpy arrays 
            where each row is a birth/death interval for a feature.

            If for some reason parsing the input fails, the output 
            will be a list of strings containing the lines of the 
            output from ripser.

    '''
    import re
    import numpy as np

    if type(fname)==str:
        f = open(fname,'r')
        lines = f.readlines()
        f.close()
    elif type(fname)==list:
        lines = fname
    #

    expr_PHdim = 'persistence intervals in dim ([\d]):'
    expr_interval = '\ [\[\(]{1,}(.*),(.*)[\]\)]{1,}'

    prog_PHdim = re.compile(expr_PHdim)
    prog_interval = re.compile(expr_interval)

    PH_intervals = {}

    for line in lines[2:]:
        if re.match('value range', line):
            # This is a line describing the range of epsilons measured.
            # Expected that this is a header line. Skip to the next line.
            continue
        #

        m = prog_PHdim.match(line)
        if m!=None:
            # initialize a new dictionary entry for the new PH dimension
            dim = int(m.group(1))
            PH_intervals[dim] = []
        else:

            m = prog_interval.match(line)
            if m==None:
                print('Warning: could not match the following line: ')
                print(line)
                print("It's probably nothing.")
                continue
            #
            left = np.double(m.group(1))
            right = np.double(m.group(2)) if m.group(2)!=' ' else np.inf
            PH_intervals[dim].append([left,right])
        #
    #
    for key in PH_intervals.keys():
        PH_intervals[key] = np.array(PH_intervals[key], dtype=np.double)
    #
    return PH_intervals
#

