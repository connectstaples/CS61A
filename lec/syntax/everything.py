## example with for loop ## simplified function 

digits = [1, 8, 2, 8]

def count(s, value):
    total = 0 
    for elem in s:
        if elem == value:
            total += 1
        return total 
# count(digits, 8) # returns 2 

     


pairs = [[1, 2], [2, 2], [2,3], [4, 4]]

for x, y in pairs: ## finding number of these pairs that have same first and second element
    if x == y:
        same_count = same_count + 1



## ranges

"""
>>> range(3, 6)
range(3, 6)
>>> range(4)[-1]
3 
"""

print(range(1, 10)) ## will output 1-9 but never last digit

## list constructor on ragne evaluates to list output 
list(range(5, 8))
"""" [5, 6, 7] """ 

list(range(4))
"""" [0, 1, 2, 3] """ 

""" Common convention for statements that never use the variable defined in name is '_' """

for _ in range(3):
    print("I am printed 3 times")

## list comprehensions in sequence processing 
"""
The general form of a list comprehension is:

[<map expression> for <name> in <sequence expression> if <filter expression>]
"""
odds = [1, 3, 5, 7, 9]
[x+1 for x in odds] # The for keyword above is not part of a for statement, 
# but instead part of a list comprehension because it is contained within square brackets.
# outputs [2, 4, 6, 8. 10]

[x for x in odds if 25 % x == 0]
# output is [1, 5]


def divisors(n):
    """
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [1] + [x for x in range(2, n) if n % x == 0]

[n for n in range(1, 1000) if sum(divisors(n)) == n]
# prints 6, 28, 496]


# reduce functools module
from functools import reduce

""" reduce(function, sequence, [initial_value]) """ 

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15

## in and not

"""
>>> 2 in digits
True
>>> 1828 not in digits
True
"""


## slicing 
"""Syntax:
sequence[start:stop:step]
"""

# getting subset of list
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [1, 2, 3]

# omitting start/stop
print(numbers[:3])   # Output: [0, 1, 2]  (First 3 elements)
print(numbers[3:])   # Output: [3, 4, 5]  (From index 3 to end)

# using step
print(numbers[::2])  # Output: [0, 2, 4]  (Every second item)
print(numbers[::-1]) # Output: [5, 4, 3, 2, 1, 0]  (Reversed list)

# Strings behave differently than than list and ranges when using in
"""
>>> 'here' in "Where's Waldo?"
True
"""

print('I am a\n new line')

## Tree recursion example 

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]

def is_tree(tree):
        """Test for if a tree has branches"""
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
        return not branches(tree)

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])]) # [3, [1], [2, [1], [1]]]
label(t) # 3

branches(t) # [[1], [2, [1], [1]]]

label(branches(t)[1]) # 2 

is_leaf(t) # False

is_leaf(branches(t)[0]) # True


def fib_tree(n):
     """
     >>> fib_tree(5)
     """
     if n == 0 or n == 1:
          return tree(n)
     else:
          left, right = fib_tree(n-2), fib_tree(n-1)
          fib_n = label(left) + label(right)
          return tree(fib_n, [left, right])


def count_leaves(tree):
     """Tree-recursive functions are also used to process trees. This function counts the leaves of a tree 
     >>> count_leaves(fib_tree(5)) # 8 
     """
     if is_leaf(tree):
          return 1 
     else: 
          branch_counts = [count_leaves(b) for b in branches(tree)]
          return sum(branch_counts)
     
def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m. Binary tree consisting of 2 choices 
    >>> partition_tree(2, 2) # [2, [True], [1, [1, [True], [False]], [False]]]
    """
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])
    
def print_parts(tree, partition=[]):
     """Printing partitions is another tree recursive function/process that traverses the tree. When truthy value found, partition printed
     >>> print_parts(partition_tree(6, 4))
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1 # root base, smallest possible parts
     """
     if is_leaf(tree):
          if label(tree):
               print('+'.join(partition))
          else: 
               left, right = branches(tree)
               m = str(label(tree))
               print_parts(left, partition + [m])
               print_parts(right, partition)

def right_binarize(tree):
    """Construct a right-branching binary tree.
    >>> right_binarize([1, 2, 3, 4, 5, 6, 7])
    [1, [2, [3, [4, [5, [6, 7]]]]]]
    """
    if is_leaf(tree):
        return tree
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]


## Linked List sections

"""
>>> four = link(1, link(2, link(3, link(4, empty))))
>>> first(four)
1
>>> rest(four)
[2, [3, [4, 'empty']]]
"""

empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))
def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]
def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]
def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]


"""So far the linked lists example do not store values in order. The following functions len_links, getitem_links 
showcase sequence abstraction (length and element selection) 

"""
def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

## len_link(four) # returns 4
## getitem_link(four, 1) # returns 2


def first(s):
    return s[0]
def rest(s):
    return s[1]
def getitem_link(s, i):
    while i > 0:
        s, i = rest(s), i-1
    return first(s)
four = [1, [2, [3, [4, 'empty']]]]
getitem_link(four, 1)


## Recursive manipulation

def len_link_recursive(s):
    """Return length of a linked list s
    len_link_recursive(four)
    4 
    """
    if s == empty:
        return 0 
    return 1 + len_link_recursive(rest(s)) # follows chain of pairs until the end of the list

def getitem_link_recursive(s, i):
    """Return element at index i of linked list s
    getitem_link_recursive(four, 1)
    2
    """
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)


def extend_link(s, t):
    """Return a list with the elements of s followed by those of t.
    >>> extend_link(four, four)
    [1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]] # notice how 'empty' isn't multiplied 
    """
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))
def apply_to_all_link(f, s):
    """Apply f to each element of s.
    >>> apply_to_all_link(lambda x: x*x, four)
    [1, [4, [9, [16, 'empty']]]] # skips over first element in list,  moves to second
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))
    

def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true.
    >>> keep_if_link(lambda x: x%2 == 0, four)
    [2, [4, 'empty']]
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

def join_link(s, separator):
    """Return a string of all elements in s separated by separator.
    >>> join_link(four, ", ")
    '1, 2, 3, 4'
    """
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)
 
def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)
    
def print_partitions(n, m):
    """
    >>> print_partitions(6, 4)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))



def tri_recursion(k):
  """
  >>> tri_recursion(6)
  1
  3
  6
  10
  15
  21
  """
  if(k > 0): 
    result = k + tri_recursion(k - 1) 
    print(result) # The print call will print the result as it iterates
  else: # once k=0, return each iteration of result to the computation of k-1. I.E. 0+1, 1+2, 3+3, 6+4, 10+5, 15+6
    result = 0
  return result

print("Recursion Example Results:")

def num_eights(n):
    """
    >>> num_eights(108)
    1
    Steps:
        1. Will check for base case if n == 0 return 0 
        2. We then return num_eights(n//10) to find its base of 0. I.E. 108//10=10 -> 10//10=1 -> 1//10 -> 0 # return 0 since n == 0 
        3. There are four frames with n updated with each iteration. Each iteration will be added to n % 10 to update the count of 8 appearing. If else, 0+0 = 0. 
        4. We return 0+0 3 times until 108 % 10=8 (returning 1+0)
    """
    if n == 0:
        return 0 
    return num_eights(n//10) + (1 if n % 10 == 8 else 0)

## How to iterate through a number n, and check the digit distance with absolute value


def digit_distance(n):
    """the digit distance is the sum of the absolute differences between consecutive digits
    >>> digit_distance(314) # 2 + 3 => 5 
    5
    Steps:
        1. n//10 for each digit to reach base case of return 0
        2. 0 returns 0 
        3. 3 returns 0 
        4. 31 becomes 3, and we add it to abs(31//10%10-n%10) which is abs(1-3) ==> 3 + 2 = 5 
        5. GAP: We dont evaluate 314. As 314 % 10 = 31 + abs(314//10%10-314%10) --> 31 + abs(1-4) ==> 31 + 3 = 33. Which is not 5 because of:
            a. abs(3-1) + abs(1-4) ==> 2 + 3 = 5 
    """
    if n // 10 == 0:
        return 0 
    return digit_distance(n//10) + abs(n//10%10 - n%10)


def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n input.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41

    Steps:
        1. Draw environment diagram, take notice for the parameters and lambda functions passed through
        2. Evaluate Return statement
            a. Pass in 1 as k for interleaved_sum_odd -> add 2+1 -> 3 -> 9 -> 5 -> 25 -> 7 # here the base case is not true so we disregard it-> 0 (ADD UP 25+9+1 = 35)
            b. Pass in 2 as k for interleaved_sum_even -> add 2+2 -> 4+2 -> 6 -> return 0 and add (4+2= 6)
        3. Return 35+6 => 41
    """
    def interleaved_sum_odd(k):
        if k <= n:
            return odd_func(k) + interleaved_sum_odd(k + 2)
        else:
            return 0

    def interleaved_sum_even(k):
        if k <= n:
            return even_func(k) + interleaved_sum_even(k + 2)
        else:
            return 0
    return interleaved_sum_odd(1) + interleaved_sum_even(2)

identity = lambda x: x
square = lambda x: x * x
triple = lambda x: x * 3 

print(interleaved_sum(5, square, identity))


def count_partitions(n, m):
    """Count the ways to partition n using parts up to m
    >>> count_partitions(6, 4)
    9
        Math:
            1. 6 = 2 + 4
            2. 6 = 1 + 1 + 4
            3. 6 = 3 + 3
            4. 6 = 1 + 2 + 3
            5. 6 = 1 + 1 + 1 + 3
            6. 6 = 2 + 2 + 2
            7. 6 = 1 + 1 + 2 + 2
            8. 6 = 1 + 1 + 1 + 1 + 2
            9. 6 = 1 + 1 + 1 + 1 + 1 + 1
    """
    if n == 0:
        return 1 
    if n < 0: 
        return 0 
    if m == 0:
        return 0 
    else: 
        return count_partitions(n-m, m) + count_partitions(n, m-1)
    


def next_smaller_dollar(bill):
    """Returns the next smaller bill in order."""
    if bill == 100:
        return 50
    if bill == 50:
        return 20
    if bill == 20:
        return 10
    elif bill == 10:
        return 5
    elif bill == 5:
        return 1

def count_dollars(total):
    """Return the number of ways to make change.
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    
    Steps:
        1. Pass in 10 into total
        2. Return 10, 100
        3. Iterate through bill to reach n == 0
        4. n will only equal 0 4 times
    """
    def make_change(n, dollar_value):
        if dollar_value == 1:  # at smallest bill, stop reducing bill size
            return 1 if n >= 0 else 0  
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            # Count ways without using this bill and ways using at least one of this bill
            return make_change(n, next_smaller_dollar(dollar_value)) + make_change(n - dollar_value, dollar_value)
    return make_change(total, 100)


def close(s, k):
    """Return the amount of times a list's index matches with its own number
    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0) # 6-0 = 6 so therefore its not Truthy.... 3 is the only index that matches with 3 
    1
    """
    count = 0 
    for i in range(len(s)):
        if abs((s[i] - i)) <= k:
            count += 1
    return count


def close_list(s, k):
    """Return a list of the elements of s that are within k of their index.
    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 1)  # 2, 3, and 5 are within 1 of their index
    [2, 3, 5]
    """
    return [s[i] for i in range(len(s)) if abs(s[i] - i) <= k] # The square brackets [] ensure that the result is a list, which matches what the function is supposed to return (a list of elements).


"""Python Interpreter
[z + 1 for z in range(10) if z % 3 == 0]
[1, 3, 6, 9]

""" 


# checking digits and iterating through them 
def double_eights(n):
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(284682)
    False
    """
    if n <= 8:
        return False
    last_digit, second_to_last_digit = n % 10, n // 10 % 10 
    return last_digit == second_to_last_digit == 8 or double_eights(n // 10)
