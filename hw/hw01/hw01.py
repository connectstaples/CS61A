from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub # iff b is negative, subtract b from a (adds its abs value)
    else:
        f = add # iff b is not negative --> add b to a 
    return f(a, b)

def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """

    # found by removing largest number from set (i,j,k)**2 
    # square and sum remaining two 
    # max operator isolates largest element (good for small groups)
    return i**2 + j**2 + k**2 - max(i,j,k)**2

def two_of_three_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    # largest factor of n that is less than n 
    # largest factor less than n is largest integer k where n%k == 0 and k < n

    for k in range(n-1,0,-1): # starts from n-1 and counts down to 1
        if n % k == 0: # checks if k is a factor
            return k # returns k (largest factor)

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    length = 1  # Initialize sequence length
    while True:  # Infinite loop, will break when n == 1
        print(n)  # Print the current value of n
        if n == 1:  # Stop when n reaches 1
            break
        if n % 2 == 0:  # If n is even
            n //= 2
        else:  # If n is odd
            n = 3 * n + 1
        length += 1  # Increment the sequence length
    return length