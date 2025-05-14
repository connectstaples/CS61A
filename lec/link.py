class Link:
        """
        >>> s = Link(3, Link(4, Link(5)))
        >>> s.first
        3 
        >>> s.rest
        Link(4, Link(5))
        >>> s.rest.rest.rest is Link.empty
        True
        >>> s.rest.first * 2
        8
        >>> print(s) # was it because we didn't reassign it, which lead to it not being updated? 
        <3 4 5>
        >>> s.rest.rest.rest is Link.empty
        True 
        """
        empty = ()
        def __init__(self, first, rest=empty):
            self.first = first
            self.rest = rest
    
        def __repr__(self):
            if self.rest:
                rest = ', ' + repr(self.rest)
            else:
                rest = ''
                return 'Link('+repr(self.first)+rest+')'
        def __str__(self):
            string = '<'
            while self.rest is not Link.empty:
                string += str(self.first) + ' '
                self = self.rest
            return string + str(self.first) + '>'