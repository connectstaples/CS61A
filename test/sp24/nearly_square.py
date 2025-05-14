def near_square(n, k):
    """
    return largest integer that is less than or equal to n and equals
    a * b for some positive integers a and b where abs(a - b) <= k

    >>> near_square(125, 0) # 11 * 11 = 121 and abs(11-11) = 0

    """

    while True:
        gap = k 
        
        while gap >= 0: 
            x = solve(gap, n)
            if x == round(x):
                return n 
            gap = gap - 1 
        n = n - 1


def solve(b, c):
    """returns largest x for which x * (x + b) = c
    >>> solve(2, 120) # x = 10 solves x * (x + 2) = 121
    10.0
    """
    return (b*b/4 + c) ** 0.5 - b/2