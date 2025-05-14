# these two functions do the same operation. 
# Function fact_iter can be less easier to explain than fact. 
# Proving that recursion is sometimes less complicated than iteration

def fac_iter(n):
    total, k = 1, 1 # init starting variables to 1
    while k <= n: 
        total, k = total * k, k + 1 # while n is greater than k; add k + 1 to variable k, and total * k for variable total 
    return total 

def fact(n):
    if n == 0:
        return 1 
    else:
        return n * fact(n-1) # recursion happens here, calling itself within itself