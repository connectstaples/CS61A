def repeating(t, n):
    """This function checks the number of digits(t) to form positive integer n that repeat 
    >>> repeating(1, 6161) # no one digit repeating will always be false
    False
    >>> repeating(2, 6161) # repeating in 2 digits implies truthy 
    True
    >>> repeating(3, 6161) # no 3 digit repeating sequence 
    False
    >>> repeating(4, 6161) # returns itself as truthy value
    True
    >>> repeating(5, 6161) # no 5 digits
    """
    if pow(10, t-1) > n:
        return False
    rest = n
    while rest:
        if rest % pow(10, t) != n % pow(10, t):
            return False
        rest = rest // pow(10, t)
    return True 


def digits(n):
    """Return smallest m that repeats to form n
    >>> digits(6161616161)
    61
    >>> digits(3333333)
    3
    >>> digits(12312312312)
    12312312312 # returns itself
    >>> digits(123123123)
    123
    """
    k = 1
    while True:
        if repeating(k, n):
            return n % pow(10, k)
        k += 1 # keep iterating k + 1 until you find truthy value 