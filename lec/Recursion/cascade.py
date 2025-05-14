# typical structure below
def cascade(n):
    """
    >>> cascade(5)
    5
    >>> cascade(20)
    20
    2
    20
    """
    if n < 10: # base
        print(n) # base
    else:
        print(n)
        cascade(n // 10) # recursion 
        print(n)


## if two implementations are equally clear, then shorter is usually better. in this case the other function is harder to grasp 

def other_cascade(n):
    """
    >>> other_cascade(5)
    5
    >>> other_cascade(11)
    11
    1
    11
    """
    print(n) # base
    if n >= 10:
        other_cascade(n // 10) # recursion
        print(n)



# bob and alice game
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

"""
>>> play_alice(20)
Bob wins 
"""
def play_alice(n):
    if n == 0:
        print('Bob wins')
    else: 
        play_bob(n - 1)

def play_bob(n):
    if n == 0:
        print('Alice wins')
    elif is_even(n):
        play_alice(n - 2)
    else:
        play_alice(n - 1) 