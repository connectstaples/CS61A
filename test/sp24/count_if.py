def count_if(f):
    """return a function that takes a positive integer n and returns the count of its digits for which f returns a truthy value
    >>> is_three = lambda d: d == 3
    >>> count_threes = count_if(is_three) # count_threes returns the number of threes in n
    >>> count_threes(431663334231) # 3 appears 5 times
    5
    """
    
    def g(n):
        count = 0
        while n: 
            if f(n%10):
                count += 1
            n = n // 10
        return count
    return g 

def count_at_least(k):
    """ Return a function that returns how many of the digits of its arguments a    re at least k.

    >>> above_3 = count_at_least(3) # above_3 returns the number of digits greater than or equal to 3
    >>> above_3(431663334231)
    9
    """

    return count_if(lambda d: d >= k)# count_if is called implying mutual recursive nature. n % 10 isn't needed to remove the last digit from the number and cycle through


def times(k, n, d):
    """ Returns whether n contains digits d exactly k times.
    >>>times(3, 6132344561, 4) # 4 only appears 2 times
    False
    >>>times(3, 61323445614, 4) # 4 appears exactly 3 times
    True
    """
    return k == count_if(lambda i: i == d)(n)
