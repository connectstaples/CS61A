def r(f):
    k = 2 
    k, m = k+1, f(k) # notice how m doesn't have a value. f(k) is unreachable because no binding is assigned
    return n

n = 10 
g = (lambda n: lambda k: print(k*n))(-1) # nested lambda k function has its own frame when called ## -1 is passed through outer lambda
r(g)

