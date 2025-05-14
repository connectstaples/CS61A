def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)
    
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

result = is_even(4)

# mutually recursive function can be turned into a single recursive function

def even_better(n):
    if n == 0:
        return True
    else:
        if (n - 1) == 0: # making sure to replace n with n-1 in the body of is_odd to reflect the argument passed into it:
            return False
        else:
            return is_even((n - 1)- 1) # 
