class Domino:
    def __init__(self, ns):
        self.ns = ns  # a list of two numbers

    def __repr__(self):
        return f"{self.ns[0]}-{self.ns[1]}"

    def align(self, left):
        # Mutate self so that left == self.ns[0]
        if self.ns[1] == left:
            self.ns.reverse()
        return self

def test_mutation():
    a = Domino([2, 3])
    b = Domino([4, 3])
    c = Domino([4, 5])
    line = [a, b, c]

    result = []
    current = line[0]
    result.append(repr(current))

    for d in line[1:]:
        if current.ns[1] in d.ns:
            d.align(current.ns[1])
            result.append(repr(d))
            current = d

    print(" ".join(result))

test_mutation()



## What .join built in method does in python

def what_join(): 
    """ Syntax for join method: 
    string.join(iterable)

    # works for generators as well 
    """

    # tuple example
    myTuple = ("John", "Peter", "Vicky")
    x = "#".join(myTuple)

    # dict example
    myDict = {"name": "John", "country": "Norway"} # When using a dictionary as an iterable, the returned values are the keys, not the values.
    mySeparator = " TEST "  # name TEST country # in terminal 
    b = mySeparator.join(myDict) 

    # list example 
    myList = ['John', 'Peter', 'Vicky']
    z = '#'.join(myList) 
    return z 
