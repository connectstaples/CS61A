#### Mt2, Spring 2025 Prof Denero 
## Mutability, Classes, List Comprehensions 


# Question 1 WWPD 

Key takeaways: 

1. `isinstance(<object testing>, <type>)`
    - Returns `True` if the `object` you are testing for is Truthy, False if otherwise
    - If the type parameter is a `tuple`, this function will return True if the object is one of the types in the tuple.
    ```python
    x = isinstance("Hello", (float, int, str, list, dict, tuple))

    # printing x will return `True`
    ```
2. `map(func, iterable)` is a lazy gen and **ONLY** computes when called on 
3. In a list comprehension: 
    - If the filter exp is true, you then applied the mapped exp 
4. 
```python
s = [2, [5, 8], 11]
t = [1, 3, 5, 7, 9]

def add_t(x):
    if isinstance(x, list):
        return [add_t(y) for y in x]
    else: 
        return x + t.pop()

m = map(add_t, s) 
```

1. 
```python
>>> [x[1] for x in s if isinstance(x, list)]
# [grab the first index for x in s if isinstance(x, list)]
# Output: [8]
```

2.  
```python
>>> next(m)
# Apply lazy generator and func rules 
# output: 11 # 9 + 2 
```
   - Check condition and return else statement 

3.  
```python
>>> t.pop()
# the last variable in the list is 7, we have only t.pop() 9 so far
# output: 7  
```

4. 
```python
>>> [next(m) for z in range(2)]
# call next(m) for changing_z in the index 0 and 1 
# output: [[10, 11], 12]
```
- Notice that we keep the index 0 `sublist`


# Question 2
_instructed to draw env diagram_ 
- A **list** variable is an address to an `object`. So even though a function makes a separate copy of the list variable passed to it, it can still **change** the `object` pointed to by **both variables**.

```python
def f(this):
    that = this[1]
    def g(copy):
        that[0] = 4
        copy[0] = 5
        copy[1].append(6)
        print(copy)
    g(list(this))
    this.append(that)
    that.append(7)

t = [1, [2], 3]
f(t)
print(t) 
```
1. What is displayed by the call to `print` on line 7? 
```python
[5, [4, 6], 3]
```

2. What is displayed by the call to `print` on line 14? 
```python
[5, [4, 6, 7], 3, [4, 6, 7]]
# answer is: [1, [4, 6, 7], 3, [4, 6, 7]]
```

3. What is the order of growth it takes to execute `result = nest(n)` in terms of the positive integer `n`? Assume that `append` always takes one step `constant time` 

Options: 
- Linear
- Quadratic
- Exponential 
- Logarithmic 
- Constant 

Answer: 
**Linear**
- We are using a for loop that increments by 1, and doubles the amount of input 

_Why other options are wrong_
- Quadratic requires input that is being quadrupled 
- Exponential scales without bound (infinite recursion can be slow)
- Logarithmic time scales efficiently **Does not answer why** 
- Constant time will not increase in time based on input
```python
def nest(n):
    """Create a nested list.
    >>> nest(3)
    [[[[], []], [], [[], []]], [[[], []], [[], []]]]
    """
    s = []
    first = s
    for x in range(n):
        next_s = []
        s.append(next_s)
        s.append(next_s)
        s = next_s
    return first
```