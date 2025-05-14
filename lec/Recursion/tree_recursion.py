from ucb import trace

@trace
def fib(n):
    """
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    2
    >>> fib(10)
    55
    """
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
    

# other example
def fib(n):
    if n == 1:
        return 0 
    if n == 2:
        return 1
    else:
        return fib(n -2) + fib(n - 1)
result = fib(6)


