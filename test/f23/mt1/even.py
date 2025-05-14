def even(f, n):
    """Return whether f(n) is even"""
    even = False # even is bound to False in global frame
    def check(h):
        if h(n) % 2 == 0:
            even = True # even is bound to True in local f1 func check(h)
        check(f)
        return even
n = 2 
even(lambda m: m + n, 4) # h is bound to a lambda function 
# lambda m: 4 + 6 
# check(6) 

"""
This program always returns False regardless of the value of f(n) even if true 
"""