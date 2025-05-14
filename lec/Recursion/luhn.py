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

# mutual recursion example is when both functions call on each other

"""
>>> luhn_sum(2)
2
>>> luhn_sum(32)
8
>>> luhn_sum(5105105105105100)
20

"""
def luhn_sum(n):
    if n < 10:
        return n
    else: 
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last
    
def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
    
