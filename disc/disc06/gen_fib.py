def mult_partition_gen(n, m):
    """Yield multiplicative partitions of n using factors up to m.

    >>> for partition in sorted(mult_partition_gen(12, 4)):
    ...     print(partition)
    "1 * 12"
    "2 * 2 * 3"
    "2 * 6"
    "3 * 4"
    """
    assert n > 1 and m > 1
    if n == m:
        yield str(n)  # Simplest partition: just n itself when n equals m
    if n % m == 0 and n > m:
        # Use m as a factor, then partition n // m
        for sub_partition in mult_partition_gen(n // m, m):
            yield f"{m} * {sub_partition}"
        # Also yield m directly multiplied by the quotient if no further partitioning
        yield f"{m} * {n // m}"
    if m > 2: # when it is 1, it spits an error. so we skip base case 
        # Skip m and try smaller factors
        yield from mult_partition_gen(n, m - 1)
