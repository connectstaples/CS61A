def split(n):
    """
    >>> all_but_last, last = split(2013)
    201
    >>> last
    3 
    """
    return n // 10, n % 10 


def sum_digits(n):
    """
    >>> sum_digits(2013)
    6
    >>> sum_digits(123456789)
    45
    """
    if n < 10: # conditional statements check for base cases
        return n # base cases are evaluated without recursive calls 
    else: # below is the recursive call
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last
    
# recursion and iteration example 

def sum_digits_iter(n):
    """
    >>> sum_digits(2013)
    6
    >>> sum_digits_iter(2013)
    6
    """
    digit_sum = 0 
    while n > 0: 
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum 