def times(k, n, d):
    """ Returns whether n contains digits d exactly k times.
    >>>times(3, 6132344561, 4) # 4 only appears 2 times
    False
    >>>times(3, 61323445614, 4) # 4 appears exaclty 3 times
    True
    """
    return k == count_if(lambda i: i == d)(n)
