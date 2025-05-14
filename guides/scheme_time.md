#### Exam Prep Spring 2025 - Sultran 
# Time, Recursion, Scheme
#### Sean Villegas

# Review 
## Time Complexity 
To solve these questions: 
- how many times is a line run? 
- every function `def` or when it is called is $${O(1)}$$
- look at every single line of code, and calculate it mechanically; of how many times its executed 
- **For CS61A Exams**, these short cuts apply:
    - `while`, `for`, or `single recursion` $${\implies Linear}$$ 
- If it does not have a `while`, `for`, `single recursion` $${\rightarrow Constant}$$
- Exponential is finite, but it grows without bound
    - $${n}^2$$
- **Note:** But if the recursion and loop are nested, you're looking at **O(n²)** _(Quadratic time)_ or worse
- **Note**: In asymptotic analysis, constants and additive terms are dropped.

# 

**Mt2 Sp 2022**
### Mapping Time and Space

**Part 1** The goal of the `maplink_to_list` function below is to map a linked list `lnk` into a Python list, applying a provided function `f` to each value in the list along the way. The function is fully written and passes all its doctests.

```python
def maplink_to_list1(f, lnk):
"""Returns a Python list that contains f(x) for each x in Link LNK.
>>> square = lambda x: x * x
>>> maplink_to_list1(square, Link(3, Link(4, Link(5))))
[9, 16, 25]
"""
    new_lst = []
    while lnk is not Link.empty:
        new_lst.append(f(lnk.first))
        lnk = lnk.rest
    return new_lst
```

What is the order of growth of `maplink_to_list1` in respect to the size of the input linked list lnk?
- Constant
- Logarithmic
- Linear 
- Quadratic 
- Exponential 

**<center>To Solve</center>**

- $${len(list) \implies O(n)}\$$
- `while` loop will execute based on input size of n 
    - Thus implying that it grows **Linearly**

# 

**Part 2** 
The next function, `maplink_to_list2`, serves the same purpose but is implemented slightly differently. This alternative implementation also passes all the doctests.

```python
def maplink_to_list2(f, lnk):
    """Returns a Python list that contains f(x) for each x in Link LNK.
    >>> square = lambda x: x * x
    >>> maplink_to_list2(square, Link(3, Link(4, Link(5))))
    [9, 16, 25]
    """
    def map_link(f, lnk):
        if lnk is Link.empty:
            return Link.empty
    return Link(f(lnk.first), map_link(f, lnk.rest))

    mapped_lnk = map_link(f, lnk)
    new_lst = []
    while mapped_lnk is not Link.empty:
        new_lst.append(mapped_lnk.first)
        mapped_lnk = mapped_lnk.rest
    return new_lst
```
What is the order of growth of the alternative function, `maplink_to_list2`, in respect to the size of the input linked list `lnk`?

- Constant
-  Logarithmic
-  Linear
-  Quadratic
- Exponential


**<center>To Solve</center>**

- $${len(list) \implies O(n)}\$$
- We have two lists 
- `while` loop will execute based on input size of n 
    - Thus implying that it grows **Linearly**
- **Note:** But if the recursion and loop are nested, you're looking at O(n²) or worse
- **Note**: In asymptotic analysis, constants and additive terms are dropped. So even tho the above function has single recursion and a while loop that grows both on input of size n, $${O(n) + O(n) \implies O(n)}$$

# 

### class `Link`, Recursion, Indexing and Mutating Lists 
Implement `make_necklace`, a function that creates a linked list where each value comes from a given list of beads, and the beads are repeated in order to make a necklace of a given length.

For example, if `make_necklace` is called with `["~", "@"]` and a length of 3, then the linked list will contain `'~', then '@', then '~'`

```python
    def make_necklace(beads, length):
    """
    Returns a linked list where each value is taken from the BEADS list,
    repeating the values from the BEADS list until the linked list has reached
    LENGTH. You can assume that LENGTH is greater than or equal to 1, there is
    at least one bead in BEADS, and all beads are string values.
    >>> wavy_ats = make_necklace(["~", "@"], 3)
    >>> wavy_ats
    Link('~', Link('@', Link('~')))
    >>> print(wavy_ats)
    <~ @ ~>
    >>> wavy_ats2 = make_necklace(["~", "@"], 4)
    >>> print(wavy_ats2)
    <~ @ ~ @>
    >>> curly_os = make_necklace(["}", "O", "{"], 9)
    >>> print(curly_os)
    <} O { } O { } O {>
    """
    if __________:
        return __________

    return Link(__________, make_necklace(__________, __________))
```

**<center>To Solve</center>**
- appending returns none, which is not good 
- pop will not return none 
- We are repeating the values until the linked list has reached the length specified. Draw out the pattern
- You have a base case
- I first went for `length - 1` because you need to decrement the length to reach a base case of `Link.empty`
- `if length == 0` or `if length > 1` are both valid 
- **Note**: you cannot add a value to a list. e.g.
    ```python
    lst = [1, 2]
    lst + 3 # returns error 

    lst + [3] # will work
    ```
- Understand when cycling through a list, that if you want to preserve the elements, then use indexing for just a value.
    - Use slicing to allow for mutation to that list e.g. `[1:]`


### Scheme
You are writing a function that performs one of four arithmetic operations -- add, subtract, multiply, division - based on the values of a and b passed. If a is greater than b, add the two together. If a is less than b, subtract b from a. If both are equal and both are even, multiply them. Otherwise, divide them


```scheme
(define (calculate a b) 
    ((cond 
    (() +)) 
    (() -)) 
    (() *) 
    (else ())
    a b)

(define (calculate a b) 
    ((cond 
    ((> a b) +)) 
    ((< a b) -)) 
    ((= a b and even?) *) ; ((and (= a b) (even? n)))
    (else (/))
    a b)
```


**<center>To Solve</center>**

- Ask yourself which syntax is wrong
- All scheme requires () to evaluate 
- `even? n` checks if the sum is even **(built in function)**
- `odd? n` checks if the sum is odd **(built in function)**
- Notice the operator outside of the evaluated expressions 
- else returns the operator 