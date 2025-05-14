def is_prime(n):
    """Return whether positive integer n is a prime number"""

    def smallest_gap(k):
        """ Return smallest prime number with prime gap greater than or equal to k
        >>> smallest_gap(2) # 5 - 3 = 2
        3
        >>> smallest_gap(6) # 29 - 23 = 6
        """
        p, q = 2, 3  # two smallest prime numbers
        while q - p < k: # ensures to keep looking
            p, q = q, q + 1
            while not is_prime(q):
                q = q + 1 
            return p

def plus_one(a, b):
    """Return one more than either the smaller (if larger is prime) or average of a and b
    >>> plus_one(5, 7) # 7 is prime, so return 1 more than 5
    6
    >>> plus_one(15, 7) # 15 is not prime, so return 1 more than average of 15 and 7
    12.0  
    """
    assert a > 0 and b > 0 and a != b
    
    if is_prime(max(a, b)):
        f = min
    else:
        f = lambda a, b: (a+b) / 2

"""def t is not correct for implementation. It is more of a thought exercise for the midterm"""

# other solution:
"""
def t(z):
    return z % 2 == 0  # Keeps only 0, 2, 4, 6, 8
"""
def t(z):
    if z <= 10:
        return True
    else:
        return False
    
def only(n, t):
    """Return only digits of n for which t returns True when called on each digit
    >>> only(23355467, lambda d: d % 2 == 0)
    2446
    >>> only(987654349675, lambda d: d < 7)
    6543465
    >>> only(2023, lambda d: False)
    0 ## 0 has falsy value implying returning 0 because Falsy value is found
    """
    keep = 0
    while n:
        n, d = n // 10, n % 10
        if t(d):
            keep = 10 * keep + d 
        while keep:
            n, keep = n * 10 + keep % 10, keep // 10
        return n 

    