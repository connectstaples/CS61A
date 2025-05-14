def changes(n):
    """Return number of adjacent digits that are different in dice number n. (checks from left) 
    >>> changes(22222)
    0
    >>> changes(222255)
    1
    >>> changes(22322)
    2 
    >>> changes(22366666622)
    3
    >>> changes(52431)
    4
    """

    count = 0

    while n >= 10:
        if n % 10 != (n // 10) % 10:
            count = count + 1
        n = n // 10
    return count 
 
