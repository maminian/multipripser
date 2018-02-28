def create_distmat_str(D):
    '''
    Converts a lower triangular matrix to a raw string csv.
    '''

    n = len(D)
    outstr = ''

    for i in range(n):
        line = ''
        for j in range(i):
            line += '%.15f,'%D[i,j]
        #
        line += '\n'
        outstr += line
    #
    outstr = outstr.encode()
    return outstr
#
