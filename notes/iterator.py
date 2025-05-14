def ring(s):
    """Yield all values of non-empty s in order, repeatedly to exhaustion
    >>> t = ring([2, 5, 3])
    >>> [next(t), next(t), next(t), next(t)]
    """
    while True:
        yield from s 

def fork(t):
    """Return two iterators with the same contents as infinite iterator t
    >>> a, b = fork(ring([1, 2 3]))
    >>> [next(a), [next(b), next(b), next(b)], next(a)]
    [1, [1, 2, 3], 2]
    """
    s = []
    def copy(): 
        i = 0
        while True: 
            if i == len(s):
                s.append(next(t))
            yield s[i]
            i += 1 
        return copy(), copy()
