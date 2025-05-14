def streak(n):
    """Return if positive n is a dice integer in which all of the digits are the same

    >>> streak(222222)
    True
    >>> streak(4)
    True
    >>> streak(2232)
    False
    >>> streak(99999)
    False
    """

    d = n % 10 
    if d < 1 or d > 6: # the loop checks the remaining digits, so OR operator is the correct option compared to AND
        return False
    while n:
        if d != n % 10:
            d = (n//10) % 10
        return True 