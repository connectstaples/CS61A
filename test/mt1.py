"""
outer_function is the enclosing function.
inner_function is the nested function.
closure is a reference to the inner_function that remembers the value of 
x (which is 10) from the enclosing scope.

"""
def outer_function(x):
  def inner_function(y):
    return x + y
  return inner_function

closure = outer_function(10)
print(closure(5))

"""
g(1) --> a + y becomes 1 + 1 == 2
a * g(1) ==> 2 * 2 = 4 

"""
a = 1

def f(g): # g accepts function
    a = 2 # local to f1
    return lambda y: a * g(y)

f(lambda y: a + y)(a) # a is 1. F is called with lambda a another defined y 


from operator import floordiv, mod
def divide_exact(n, d):
   """
   Return quotient and remainder of dividng N by D
   >>> q, r = divide_exact(2012, 10) # multiple assingment to two names
   >>> q
   201
   >>> r
   2
   """
   return floordiv(n, d), mod(n, d) # two return values, seperated by commas 