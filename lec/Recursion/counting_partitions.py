def count_partitions(n, m):
    if n == 0: 
        return 1 
    elif n < 0: 
        return 0 
    elif m == 0:
        return 0 
    else:
        with_m = count_partitions(n -m, m)
        without_m = count_partitions(n , m-1)
        return with_m + without_m 

result = count_partitions(5, 3)


# other solution

def count_partitions_other(n, m):
    """ Count ways to partition n using parts up to m
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions_other(n - m, m) + count_partitions_other(n, m -1)


# without recursion 
def dynamic_partitions(n, m):
    """
    Calculate the number of ways to partition n using parts up to size m.
    This implementation uses dynamic programming to avoid recursion.

    >>> dynamic_partitions(6, 4)
    9
    """
    # Create a table to store results of subproblems
    # dp[i][j] will store the number of ways to partition i using parts up to j
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: There is 1 way to partition 0 (using no parts)
    # This is true for any value of j (parts up to j)
    for j in range(m + 1):
        dp[0][j] = 1

    # Fill the table using dynamic programming
    for i in range(1, n + 1):  # Iterate over all values of n (from 1 to n)
        for j in range(1, m + 1):  # Iterate over all values of m (from 1 to m)
            if j > i:
                # If the part size j is greater than n (i), we can't use j
                # So, the number of partitions is the same as using parts up to i
                dp[i][j] = dp[i][i]
            else:
                # Otherwise, the number of partitions is the sum of:
                # 1. Partitions that include at least one part of size j (dp[i - j][j])
                # 2. Partitions that do not include any part of size j (dp[i][j - 1])
                dp[i][j] = dp[i - j][j] + dp[i][j - 1]

    # The result is stored in dp[n][m], which gives the number of partitions of n using parts up to m
    return dp[n][m]