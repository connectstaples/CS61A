x, y = 1, 2

def this(x):
    x = 3
    print(y)
    return 4 
def which(x, f):
    def this(x):
        x = 5
        return y 
    y = 6 
    y = f(x)
    print(this(y))
    return lambda: (print(x) or y)

print(which(7, this)())

