def single_sequence_scaling(measure,seq=[],**kwargs):
    '''
    This script generates ONE point cloud and goes through
    the usual process of generating data for a log-log plot,
    based on nested subsets of the point cloud.

    Advantage: only one distance matrix computation is needed
    for a sequence of points, so this is only
    bottlenecked only by ripser.

    Inputs:
        measure: The probability measure to sample from
        npoints: The maximum number of points to use
    Optional inputs:
        seq: A sequence of integers up to npoints
            specifying the subsets of the data to work
            with. Default: [2,3,...,npoints].
        nprocs: Number of processes to use for the parallization

        All other inputs are passed to the measure function.

    Outputs:
        results: A dictionary with keys being number of points;
            values being dictionaries of bar codes in the number
            of PH dimensions.

    '''
