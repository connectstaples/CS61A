"""
    f(x): Subtracts one from an integer x. For example, f(5) is 4.
    g(x): Adds one and then doubles an integer x. For example, g(5) is 12.
    h(x, y): Concatenates the digits of two different positive integers x and y. For example, h(789, 12) evaluates to 78912 and h(12, 789) evaluates to 12789.

Definition: A small expression is a call expression that contains only f, g, h, the number 5, and parentheses.
All of these can be repeated. For example, h(g(5), f(f(5))) is a small expression that evaluates to 123.

What's the shortest small expression you can find that evaluates to 2025?

Nested function call:
    init 5
    build that 5 to 12 when you call g
    hand it to h 
    h is a func that takes 2 params x, y 
        how do u achieve 20 building up from 5? 
"""

def subtract(x):
    return x - 1
subtract 

def add_multiply(g):
    sol = (g + 1) * 2
    return sol
add_multiply


f(g(h(5,5)))

# went for 2026 first and subtracted 1 



# Devons solution

def f(x): x-1
	
def g(x): (x+1)*2

def h(x,y): x.y


# Solution:
# * g(h(g(5),5))
# 1. g(5) = 12
# 2. h(12,5) = 125
# 3. g(125) = 252

# h.
# (g(f(f(f(g(5))))), f(g(g(5))))
# 1. g(5) = 12		1. g(g(5)) = 26
# 2. f(f(f(12))) = 9  2. f(26) = 25
# 3. g(9) = 20

# ---> h(20,25) = 2025