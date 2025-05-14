## Link Class from CS61a

```python
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
```

## Rules
1. You do not need to explicitly pass in Link.empty every time you call the Link class in CS61A. The Link class is designed so that the rest parameter defaults to Link.empty if you do not provide it.
    - So, you only need to pass Link.empty if you want to be explicit, but it is not required for the last element since the default is already Link.empty
2. If you try to pass something that is not a Link or Link.empty as the rest parameter, you will get an AssertionError