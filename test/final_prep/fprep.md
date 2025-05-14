#### CS61A Sp25 Prof Denero
# Final notes 2025
#### Sean Villegas
#### F25, F21, Sp24

[f24 Final Sol](https://cs61a.org/exam/fa24/final/61a-fa24-final_sol.pdf)

[Tree Recursion & n//10 OR n%10 functionality](https://www.youtube.com/watch?v=LGtai0ottUc)

<style>
.tnr {
  font-family: 'Times New Roman', serif;
  font-size: 15px;
}

</style>


# Fall 2024 

## Python Lists

**Question 1 WWPD?**

_generators and lists_ 

### Where I went Wrong

### Where I went Right

### Hindsight 20/20 

#

<details><summary>Question 2 Line Diagram</summary>

_mutating lists environment diagram_ 

```python
b = 6
log = []

def make_line(a):
    b = 1
    list(log).append(a)
    return lambda x: a * x + b 
def shift_line(f):
    b = 3
    log.append([b])
    return lambda y: f(y) + b

z = shift_line(make_line(2))(0)
print(log)
print(z)
```
<div class="tnr">

**Questions:**
- What is displayed by print(log) on line 15?
- What is displayed by print(z) on line 16?

</div>

### Where I went wrong
1. At first, I tried evaluating outer frame which was wrong method of attack 
### Where I went right
2. Re-evaluate, employ _pemdos_ 
3. When local functions use `append` with the same variable names $\rightarrow$ the interpreter evaluates the which variable to pull from, i.e. local or parent. 
    - when appending a variable symbol to a list, it will automatically evaluate that variable that is binded to the symbol 
4. `list(lst)` will make a deep copy of a list if it has a list passed within
    - **deep copy:** is a copy that recursively evaluates every element in the list and makes its own independent list without using a reference (i.e. a pointer) to original list
    - **shallow copy:** is a copy of the original first level elements, any sub-operands (i.e. lists within lists) are pointers to the original list, and therefore can be mutated and reflect changes to the original list 
5. `append` with brackets around variables passed in $\Rightarrow$ means you add the bracketed value to a single index 
6. `extend` with brackets around variables passed in will always just add the elements. As that is the functionality of `extend`
7. Ask what is local memory v.s. outer memory
8. The outer parenthesis in a function call will remain even after first use $\Rightarrow$ can be used in other lambda or def statements within the function its next to, when a function needs a variable to process
    ```python
    shift_line(make_line(2))(0) 
    ```

# 

</details>

<details><summary>Question 3 Make Tense</summary>


<div class="tnr">
A list of numbers is easier for a person to sum up if it can be split into groups that all sum to 10. Implement
tens, which takes a list of positive numbers s. It returns True if, for every positive integer i where 10 * i <=
sum(s), there is a positive k that satisfies sum(s[0:k]) == 10 * i. Otherwise, it returns False.
</div>

```python
def tens(s):
    """Return whether every multiple of 10 less than or equal to sum(s) appears as a prefix of s.
    >>> tens([3, 2, 2, 3, 6, 2, 2, 4, 1, 5, 2]) # sum(s[:4])==10, sum(s[:7])==20, sum(s[:10])==30
    True
    >>> tens([3, 2, 2, 3, 6, 2, 6, 1, 5, 2]) # sum(s[:4])==10, but no slice starting at 0 sums to 20
    False
    """
    t = 0
    for x in s:
        t += x
        if _______:
            return _______
        if t == _______:
            t = _______
    return True
```

### Where I went wrong
1. I assumed we would take the sum within the code based on the docstring comments
2. I thought this would require recursion

### Where I went right
1. I correctly assumed that we had base cases to check for an element
2. I knew we had to return False in one of the base cases 
3. 
    ```python
    t += x  # <=> is shorthand for t = t + x 
    ```

### Hindsight 20/20 
1. Prefix sums $\Rightarrow$ cumulative total starting from the beginning of the list 
    - compared to incrementing _down_ from right side with 
    ```python
    x // 10 % 10 
    ```
    - cumulative sums $\Rightarrow$ running total 
2. The `for` loop in the skeleton code denotes we use an incremental step of adding each element to the the counter `t`, and check with our base cases on that element added to `t`
3. You must understand when the counter must be reset in the `True` case
</details>

# 

## Classes and OOP 

<details><summary>Question 4(a) Count Misses</summary>
<div class="tnr">
Implement the Counter class. A Counter has a count of the number of times inc has been invoked on
itself or any of its oﬀspring. Its oﬀspring are the Counters created by its spawn method or the spawn
method of any of its oﬀspring.
</div>

```python
class Counter:
    """Counts how many times inc has been invoked on itself or any of its offspring.
    >>> total = Counter()
    >>> odd, even = total.spawn(), total.spawn() # these are offspring of total
    >>> one, three = odd.spawn(), odd.spawn() # these are offspring of odd and total
    >>> for c in [one, even, three, even, odd, even]:
    ... c.inc()
    >>> [c.count for c in [one, three, even, odd, total]]
    [1, 1, 3, 3, 6]
    """

    def __init__(self, parent=None):
        self.parent = parent
        _______

    def inc(self):
        self.count += 1
        _______:
            _______

    def spawn(self):
        return _______
```

### Where I went Wrong
1. I added another count that performed addition to self.count in the loop 

### Where I went Right
- _Employed Process of elimination_ 

1. Understood through pattern matching that we need a `self.count = 0`
2. Understood that we need to check a condition once based on the parents inits
3. Understood the correct conditional v.s. loop
    - `while` would need some way to check when it fails to exit the loop, skeleton code doesn't allow for that
    - `for` needs some iteration in the options given, and the choices given do not have an iterable 
4. Understood that we need to initialize and return another object when we call the `spawn` method based on the options 

### Hindsight 20/20 
**OOP and Parent Child Relationships:**
- The `Counter` class shows how a parent object can influence its child objects by passing method calls upward (via the parent reference). This is key to designing objects that are hierarchical in nature.
    - The `inc()` method uses recursion to propagate (i.e. spread over all objects) the count increment through the parent chain. 
    - This is a fundamental idea where an action (in this case, incrementing the count) needs to be passed upward through a **chain of objects** (the parent-child relationship).

**Conditionals v.s. Loops:**
- Know when to use `if` vs. `while` vs. `for`.
1. `if` is for checking a condition once and taking action based on that condition.
2. `while` is for continuous looping until a condition fails. 
3. `for` is for iterating over a **collection of items**. 
    - In this problem, we don’t need a loop; we need a simple conditional check.

</details>

# 

<details><summary>Question 4(b) MissDict</summary>

<div class="tnr">
Implement the MissDict class. A MissDict has a dictionary d. Its get method takes an iterable keys, returns a list of all values in d that correspond to those keys, and counts the number of keys that did not appear in d (called misses). Printing a MissDict displays a fraction in which:

- The numerator is the number of misses during all calls to get for that particular MissDict instance.
- The denominator is the number of misses during all calls to get for any MissDict instance.

Assume Counter is implemented correctly.
</div>

```python
class MissDict:
    """Has a dict, gets a list of values for an iterable of keys,
    and counts the number of keys that are not in the dict.
    >>> double = MissDict({1: 2, 2: 4, 3: 6, 5: 10})
    >>> half = MissDict({2: 1.0, 3: 1.5, 4: 2.0})
    >>> double.get([1, 3, 5, 2, 4]) # No value for key 4 (1 miss)
    [2, 6, 10, 4]
    >>> double.get([5, 4, 3, 0, 4]) # No value for keys 4 or 0 or 4 (3 misses)
    [10, 6]
    >>> half.get([1, 3, 5, 2, 4]) # No value for keys 1 or 5 (2 misses)
    [1.5, 1.0, 2.0]
    >>> print(double) # double had 4 misses & half had 2 misses
    4/6 of the misses
    """
    misses = Counter()
    def __init__(self, d):
        assert isinstance(d, dict)
        self.d = d
        self.misses = _______

    def get(self, keys):
        result = []
        for k in keys:
            if k in self.d:
            _______
        else:
            _______
        return result

    def __str__(self):
    return f'_______ of the misses'
```


### WIW/R

`self.misses` variable
- I understood that we needed to init the `Counter()` class through `spawn` method. 
- There was another option with different syntax that achieves the same effect
    `MissDict.misses.spawn()` $\equiv$ `Counter(MissDict.misses)`

`for k in self.d:` 
- I understood that we needed to somehow add the values of the k dictionary look up to the `result` list. At first thought it was a dictionary comprehension, then I thought list comprehension, then I understood it was an append call with a classic `dictionary[key]` method that would get appended to result 
    - dictionary comprehension creates a dictionary based on values in iterable
    - list wouldn't make sense here since we already have a list. But, it is possible
    ```python
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    keys = ['a', 'c']

    values = [my_dict[key] for key in keys]
    print(values)  # Output: [1, 3]
    ```

`self.misses.inc()`
- We call the above method for self.misses to create a spawn of all the misses. I was torn between two choices:
    - `self.misses.inc()`
    - `self.misses.count += 1`
- `self.misses.count += 1` is wrong, because it increments already by itself through each parent call to spawn and inc. 
    - It would only increment the local counter
    - It wouldn't trigger the parent counter to increment
    - We'd lose the automatic parent-child counting that makes the Counter class work

`{self.misses.count} / {MissDict.misses.count}`
- My first attempt I looked for each option that had a `.self` in its name. 
- However, rereading the problem lets us know that the numerator is supposed to be the instance misses count divided by the total misses count, in string format 
- I understood we had to use `{}` to get desired output. 

### Hindsight 20/20 

`self.misses.count += 1` 
- It would only increment the local counter
    - It wouldn't trigger the parent counter to increment
    - We'd lose the automatic parent-child counting that makes the Counter class work

- This does the same thing

    `MissDict.misses.spawn()` $\equiv$ `Counter(MissDict.misses)`

`NewClass.classvar.parentmethod()` $\equiv$ `ParentClass(NewClass.classvar)`

- `classvar` is an instance of ParentClass
- `method()` is a method that creates a new instance with the current instance as parent
- The right side directly creates a new instance with the parent specified

#

</details>


<details><summary>Promotion to CS 61B</summary>

<div class="tnr">
Given a sequence s and positions (indices) i and j in s with i < j, promoting an element to i from j means reordering s so that the element originally at position j is now at position i, all elements originally positioned between i and j increase their position (index) by one, and all other elements stay where they are. The beginning of s is position 0. 

<br>

For example, in the list [30, 60, 90, 120, 150, 180], promoting
to 2 from 4 would place the number 150 (original position 4) just before 90 (originally position 2) and increases the positions of both 90 and 120 by one, resulting in [30, 60, 150, 90, 120, 180].

Implement promote, which takes a list of numbers s and two non-negative integers i and j. It returns a new list promoting to i from j in s. Do not mutate s.

- Hint: For any list `s, s[len(s):]` evaluates to `[]`.
</div>

```python

def promote(s, i, j):
    """Return a list in which s[j] is at index i without mutating s.
    >>> promote([3, 6, 9, 12, 15, 18], 2, 4)
    [3, 6, 15, 9, 12, 18]
    >>> promote([3, 6, 9, 12, 15, 18], 0, 4)
    [15, 3, 6, 9, 12, 18]
    """
    assert i >= 0 and i < j and j < len(s)
    return s[:i] + _______ + _______ + s[_______:]

```

### WIW/R
- I knew we are making deep copies (so we dont mutate the original s list)
- I saw a pattern and went through all options of computation, but with `indexing` as a **slicing** rather than `range` selection
- I correctly deduced that slicing an element would just return a number, and adding that number would result in an error when adding lists
- `Extend` and `Append` mutate lists

### Hindsight 20/20 
- The big idea is that slicing works like range
    - i.e. `range(start, stop)` compared to python list indexing which returns the elements that you specify 
- Correct term is shallow copy, as `list`, and indexing i.e. `[:]` or `[i:]`creates shallow copy. 
- Append does not flatten or unpack the contents.
    - i.e. it will keep the list brackets and it adds contents to end of list, via indexing 
    - It adds object
- `+` combines lists by unpacking their elements.
- `Append` and `Extend` both return None
- **Slicing creates a new object** 

</details>


#

### Tree Class
<details><summary>Fresh Produce</summary>

<div class='tnr'>
Implement products, which takes a Tree instance t with positive integer labels and a positive integer n.
It returns True if every path from the root of t to a leaf has labels that equal n when multiplied together.

</div>

```python
def products(t, n):
    """Return whether the product of labels along every root-to-leaf path is n.
    >>> products(Tree(1, [Tree(2, [Tree(3)]), Tree(6)]), 6)
    True
    >>> products(Tree(1, [Tree(2, [Tree(3)]), Tree(6)]), 12)
    False
    >>> products(Tree(1, [Tree(2, [Tree(3)]), Tree(5)]), 6)
    False
    >>> products(Tree(1, [Tree(5, [Tree(2)]), Tree(12)]), 12)
    False
    """
    assert type(n) == int
    if t.is_leaf():
        return _______
    if _______:
        return False
    
    return _______
    (c)
```

#### WIW
- I thought that we would return True, because is_leaf() returns false if .branches is empty, but actually it returns True when it is empty because thats when it is a leaf, and false if others (if it has branches)
- For the recursive function, I passed in the list comprehension as the second argument, but really it was supposed to execute based on the list comprehension 
    - `product(t, [n * b.label] for b in t.branches]`

#### WIR
- I understood that we would return `False` if the product of `n % t.label > 0` 
- I understood that we had a recursive call to products, with the second argument to products being an integer. 

#### Hindsight 20/20 
Functions that aggregate iterable argument (on study guide): 
- `all(iterable)` returns bool for all values 


</details>

<details><summary>Produce</summary>


<div class='tnr'>

Implement produce, which takes a positive integer n. It returns a Tree of positive integers in which:

- The product of the labels along every root-to-leaf path is n,
- Every increasing sequence of integers starting with 1 that has product n is a root-to-leaf path, and
- Every sequence of siblings (nodes with a common parent) is an increasing sequence.

</div>

```python
def produce(n):
    """Return the largest tree in which the labels for every root-to-label path
    are increasing and have product n. Put all siblings in increasing order.
    >>> produce(12)
    Tree(1, [Tree(2, [Tree(6)]), Tree(3, [Tree(4)]), Tree(12)])
    >>> print(produce(24)) # Paths are 1-2-3-4, 1-2-12, 1-3-8, 1-4-6, and 1-24
    1
    2
    3
    4
    12
    3
    8
    4
    6
    24
    """
    def grow(t, x):
        for k in range(_______, x + 1):
            if _______ % k == 0:
                branch = _______
                
                if _______:
                    t.branches.append(branch)
        return t

    return grow(Tree(1), n)
```


#### WIW
- Misunderstanding of the idea, I thought we would have to do some sort of mod and then floor division to grab the first element
    - Instead we simply compare `if x % k == 0` at each iteration of the range to then see if we append it to the `tree.branches`
- Thought we were interacting with the `products` function defined earlier (notice that its missing a "assume a func is implemented correctly")
- I thought we also made a recursive call to produce, by making n smaller down. 

#### WIR
- Understood we are incrementing both t.label and x by 1 
- Understood that at each iteration, when we want to grab the `k` element in the range of `start, stop` and pass it in to `grow(t, k)`. I made a leap of faith that we would divide the count of x (as that what recursion does)


#### Hindsight 20/20 
- Before appending, we check if the branch is a leaf (we dont want a leaf), OR if `x == k `
- We do use `x % k == 0 and x // k` (in the recursive call), but not to grab the first element, rather to identify valid factors to extend the path.
- We increment `k` in the loop starting from `t.label + 1 to x`.
    -  x stays fixed during the loop, but we reduce it recursively via `x // k`

</details>


## Scheme
<details><summary>all-pairs</summary>

<div class='tnr'>

Implement the Scheme procedure all-pairs, which takes a procedure `f` and a list `s`. It returns `#t` if (f x y) is #t for every pair of adjacent elements x and y in s. Assume f always returns either `#t` or `#f`. 
</div>

```scm
(define (inc x y) (= (+ x 1) y)) ; Whether x+1 equals y
    ;;; Return #t if (f x y) is #t for every pair of adjacent values (x, y) in list s.
    ;;;
    ;;; scm> (all-pairs inc '(3 4 5 6 7 8))
    ;;; #t
    ;;; scm> (all-pairs inc '(3 4 5 8 7 8))
    ;;; #f
    ;;; scm> (all-pairs inc '(3))
    ;;; #t

(define (all-pairs f s)
    (or (null? s) (null? (cdr s))
    (and _______ (all-pairs f _______ ))))
```

### WIW
- I put the option `(apply f (car s) (car (cdr s))`
    - This assumes that the values `(car s)` and `(car (cdr s))` are a list data type (i.e. passed in and not evaluated). Reality is that these values are evaluated and not a list, breaking logic
- I chose `(cons (car s) (cdr s))`, thinking that this would continue the loop of the values in `cdr s`. 
    - The reality is, you can simply pass in `cdr s` and it will preserve the first element of `cdr s` (i.e. `car s`), and perform the same `(car (cdr s))` to compare the elements in procedure `f` 

### WIR
- I did process of elimination correctly down to 2 elements (i.e. filtered out syntax errors and the ordering of how `car` amd `cdr` work)

### Hindsight 20/20
- `(apply f s)` expects only two arguments, a function and a list data type
- In the all-pairs problem, you're not building a list manually with cons. You're just recursing down an existing list
    - Use `cons` and `nil` when constructing lists.
    - Don't use cons when just processing lists.
    - `cdr` automatically gives you the "rest of the list" — already terminated properly.


- **Question:**
    - Does cons need a `nill` if it has a provided `cdr`?
    - **Answer:**
        - No you don't. `(cons 1 2) ; => (1 . 2)`
            - The dot represents the end of a list, becoming a d**otted pair**
        - Proper list structure:
            - `(cons 1 '(2 3)) ; => (1 2 3)`



</details>

<details><summary>Show-pairs</summary>

<div class='tnr'>
Implement the Scheme procedure show-pairs, which takes a list s and returns a list of every pair of adjacent elements in s. A pair is a two-element list.


</div>

```scm
;;; Return a list of every pair of adjacent elements in list s.
;;;
;;; scm> (show-pairs '(3 5 7 9 11 13))
;;; ((3 5) (5 7) (7 9) (9 11) (11 13))
(define (show-pairs s)
    (if (or (null? s) (null? (cdr s))) nil
        ( _______ _______ (show-pairs _______ ))))

```

### WIW
- For option a I chose `list` over `cons`, as I knew that both would create a list to preserve the inner list structure
    - I thought that `cons` would expect a value, and then the *rest* of the list
- I didn't preserve the list structure for option b, which would be wrapped around `(car s) (car (cdr s))`

### WIR
- I understood that we needed a list procedure, by process of elimination I had `cons` or `list` as my option
- I got the structure for looping through the list correctly i.e. `(car s) (car (cdr s))`
- I understood that we keep the list going by calling `(cdr s)` to keep the `(car (cdr s))` as the first element in the pairs of lists


### Hindsight 20/20 
- Why `(list (car s) (car (cdr s)) (show-pairs (cdr s)))` is equivacado. `list` here creates a _flat_ list of three elements
    - The first element: `(car s)`
    - The second element: `(car (cdr s))`
    - The third element: the entire result of the recursive call `(show-pairs (cdr s))`
    - This would not preserve the pairs correctly, and we would have raw data in the list. 
- Why `(cons (list (car s) (cdr s) (show-pairs (cdr s))))` is right
    - `list` works when inside `cons`, because `(list (car s) (car (cdr s)))` will get values that `cons` accepts as the first part of the list.
        - When we hit `(null? s)` or `(null? (cdr s))` in our base - we return nill preserving the `cons` structure till completion 



<div class='tnr'>
What order of growth describes the time it takes to execute (unpair s) in terms of the length of the input list s, assuming that car, cdr, cons, and null? are all constant-time operations?
</div>

```scm
(define (unpair s) (cond ((null? s) nil)
                    ((null? (cdr s)) (car s))
                    (else (cons (car (car s)) (unpair (cdr s))))))
```

### WIR
- I understood for the time complexity question, `car`, `cdr`, `cons` and `null?` are constant and therefore adding a constant would not increase the time complexity by a some notation 
    - furthermore, we have a `cond` statement that is looping through each *element* in the list, which implies linear because 
        - Incrementing n increases time by a constant

</details>

<details><summary>all-pairs-exp</summary>

<div class='tnr'>

Implement the Scheme procedure **all-pairs-exp**, which takes a procedure name **proc-name** (a symbol) and a list s. It returns an **and** expression that calls the procedure named by **proc-name** on every adjacent pair of elements in s. Assume show-pairs is implemented correctly.

Options for first blank: 
- and
- 'and
- cons and
- cons 'and

</div>

```scm
;;; Return an and expression that calls the procedure called proc-name on
;;; every adjacent pair of elements in s.
;;;
;;; scm> (all-pairs-exp 'inc '(3 4 5 6 7 8))
;;; (and (inc 3 4) (inc 4 5) (inc 5 6) (inc 6 7) (inc 7 8))
;;; scm> (eval (all-pairs-exp 'inc '(3 4 5 6 7 8 )))
;;; #t
(define (all-pairs-exp proc-name s)
( _______ (map _______ (show-pairs s))))
```

### WIW & Hindsight
- I chose `'and` as the option, because I know that `cons` expects a value as first argument, and the rest of the list as its second. 
    - the correct option is `cons 'and` 
    - `'and` is just a symbol
    - we need: `(cons 'and list-of-expressions)`
- I thought that `map` would automatically preserve the inner list structure (i.e. not make a flat list), so I called `'inc` as my option
    - First, it was supposed to be `'proc-name`, but I made a mistake of passing in the `inc` from doctests 
    - `(map f s)` expects a function as first argument, not a symbol to be later evaluated 
    - You are supposed to pass in a lambda 
    - `(lambda (pair) (list proc-name (car pair) (car (cdr pair))))`
    - **Sudo Code:** For each pair, make a list that starts with the proc-name symbol (like inc), then the first and second elements of the pair
    - Questions: 
        - why do we pass in `proc-name` unquoted? wouldn't it compute the pair
            - **answer:**
                - because `proc-name` is already a symbol. It was passed in as a quoted symbol like `'inc`. We evaluate what proc-name is in the procedure to set it up as `inc`
            

### WIR
- I understood that we needed to pass in a list type so that scheme would construct a returned list that could be evaluated piece of code.
</details>


## SQL 
<details><summary>Arcane Jobs</summary>
<div class='tnr'>

The Council of Piltover wants a list of all the people living in regions it governs that have unique jobs. Create a table with columns labeled **name** and **job** that contains one row for each person living in a region governed by the "council" who is the only person with their job among everybody living in regions ruled by the council.
The who table has one row per person and columns for their name (string; each row has a unique value), the region (string) they live in, and their job (string). The gov table has one row per region and columns for its name called place (string; each row has a unique value) and the group that rules over it called ruler (string).


1st option: 

 (1.0 pt) Fill in blank
- who
-  who AS a, who AS b
- who, gov
- who AS a, who AS b, gov

2nd option: 
- COUNT(*) = 1
- place = "council"
- a.job = b.job
- a.job != b.job
- region = place
- a.region = place
- a.region = b.region AND a.region = place
- a.job = b.job AND a.region 

</div>

```sql
SELECT name, job FROM _______ WHERE _______ AND ruler = "council" _______ ;
```

### WIW 
- I went under the assumption that we would be performing an inner join with aliasing. So I chose option `who AS a, who AS b, gov`
    - You don’t need a self-join to find unique jobs — `GROUP BY` and `HAVING COUNT(*) = 1` does that directly.
    - Self-joins would make sense if you were comparing two people with the same job (e.g. to eliminate duplicates or find uniqueness by comparison), but grouping is more efficient and intended for this.
- I checked my answer and saw that I was wrong, so I changed option b from `a.job = b.job AND a.region = place` to `region = place`
- Part c was a fill in the blank, and it said that I could include clauses _but didnt have to_. Which made me think that it was something minimal. However, my instinct of `HAVING` was the right choice. 
    - **this is the only way to filter for uniqueness in SQL**

### Hindsight 20/20 
- Don't get thrown off from wording of problem. Step one is identify `FROM`, then `SELECT` and `WHERE` as step 2, and step 3 as `GROUP BY`, optional `HAVING`
</details>




# Classes Practice 

<details><summary>Fa21: Blink</summary>
<div class='tnr'>

Implement the Blink class. A Blink instance represents a linked list of numbers and can find the longest sublist starting with any particular value in constant time. **A Blink instance b is constructed from a linked list s (a Link instance or Link.empty)** and has the following attributes:

- b.link is s, the linked list from which b was constructed.
- b.rest is a Blink representing the rest of s. If b represents Link.empty, then it has no rest attribute.
- b.sublists is a dictionary with a key for each unique element in s. The value for a key k is the Link instance representing the longest sublist of s starting with k.
</div>

```python
class Blink:
    """A Blink has link, rest, and.sublists attributes for a linked list s.
    >>> s = Link(3, Link(1, Link(4, Link(1, Link(5)))))
    >>> b = Blink(s)
    >>> b.link is s
    True
    >>> b.rest.rest.link is s.rest.rest
    True
    >>> b.rest.rest.rest.rest.rest.link is Link.empty
    True
    >>> b.sublists[4]
    Link(4, Link(1, Link(5)))
    >>> b.sublists[1]
    Link(1, Link(4, Link(1, Link(5))))
    >>> b.rest.rest.sublists[1]
    Link(1, Link(5))
    >>> b.sublists[3] is s
    True
    """
    def __init__(self, s):
        assert s is Link.empty or isinstance(s, Link)
        if s is not Link.empty:
            self.rest = _________
                            (a)
             # Copy the sublists dict of self.rest into a new dict.
            self.sublists = self.rest.sublists.copy()
            _________
                (b)
        else:
            self.sublists = _________
                               (c)
            self.link = _________
```

(1.0 pt) Which of these could fill in blank (c)?
- self.rest.sublists
- self.rest.sublists.copy()
-  {}
- {s: s}
- {s: self}
- {s.first: s}
- {s.first: self}

iv. (1.0 pt) Which of these could fill in blank (d)?
- s
- s.rest
- s.link
- self
- self.rest
- self.rest.link

### Method of attack 
- Find problem with biggest points and see if you can work around it
- Draw link class and what instructions tell you 
</details>


# Spring 2024 Final

## Lists
<details><summary>WWPD?</summary>

<div class='tnr'>
Assume the following code has been executed. No error occurs.
</div>

```python
s = [2, 4]
t, u = [2, 0, s], [2, 0, s]
t.append(5)
u[2].extend(s)
v = t[2]
t[2] = [6, 7]
```

**Moral:** 
- `.extend` does not change object identity, it only modifies the list in-place


**Blurb:**
- in laymans terms, the pointer in memory will still be valid because we are modifying the index at that memory address, rather than _inside_ that current variable. It is true to say that the modification is happening in that list, but only because it is modifying the pointer to s
- At variables that have previous binded object identities (i.e. pointer addresses in memory), will preserve that binding unless that specific variable is modified later
- I am right to understand that when you call `.extend` with brackets, it will flatten that list and add it.
- `.append` will do the opposite, and append that preserved list element to the end creating sublists (if it is passed in as a list)
- If a variable is bound to an object (like a list), that binding is preserved unless the variable is explicitly reassigned. Other variables referencing the same object will continue to see mutations unless the object is replaced or the variable is rebound
- A variable in Python keeps pointing to the same object in memory unless it is explicitly reassigned. 
    - If multiple variables reference the same object (e.g. a list), then mutations to that object (like append, extend, pop, etc.) will be visible to all variables referencing it.
However, if you reassign the variable (e.g. x = [1, 2] or x = some_other_list), the binding changes, and the original connection is broken
- So we know that the object identity is pointing to `s` in `u[2]`, so when we `.extend(s)` at that index, it will modify the list at s (due to the pointer), and when we call print(u), that will evaluate the list elements in s.

</details>

<details><summary>List Mutation</summary>

<div class='tnr'>
Definition: The increasing sublist of a sequence of numbers s is a list containing each element of s that is larger than all previous elements. Implement up, which takes a list of numbers s and returns its increasing sublist.

Options: 
i. (1.0 pt) Fill in blank (a).
- []
- [[]]
- [s]
- [s[0]]
- None
i (2.0 pt) Fill in blank (b).
- result and s[0] < x
- result and result[-1] < x
- result or s[0] < x
- result or result[-1] < x
- not result and s[0] < x
- not result and result[-1] < x
- not result or s[0] < x
- not result or result[-1] < x
iii. (1.0 pt) Fill in blank (c).
- append
- extend
- pop
- list

</div>

```python
def up(s):
    """Return the increasing sublist of list s.
    >>> up([3, 1, 2, 5, 4, 5, 7, 6, 12, 11])
    [3, 5, 7, 12]
    """
    result = _______
            # (a)
    for x in s:
        if _______:
            # (b)
    result._______(x)
            # (c)
    return result
```

### Moral 
- Use `append` to add a single number
- Don’t use `extend` unless x is a list or iterable
- Adding a `not` in front of the result will check if it is true (i.e. when it is an empty list `[]` it is false, and we have to start the iteration by checking if it is true that it is empty when comparing it to x). When it is full, it is true, therefore it is false. 

</details>

<details>
<summary>Iterators</summary>

<div class='tnr'>

Implement upiter, which takes a finite iterator over numbers t and returns its increasing sublist. You
may not call `up` in upiter.

</div>

```python
def upiter(t):
    """Return the increasing sublist of iterator t.
    >>> upiter(iter([3, 1, 2, 5, 4, 5, 7, 6, 12, 11]))
    [3, 5, 7, 12]
    """
    try:
        x = next(t)
    except StopIteration:
        _______
    return _______ + _______ (filter( _______ , t))


def upiter(t): 
    try: 
        x = next(t)
    except StopIteration: 
        return []

    return [x] + upiter(filter(lambda y: y > x, t))
```

### WIW 
- I chose `x = []`
- I chose `list` to force the iterator to compute till exhaustion, but instead you need to make sure it filters each time for every new `[x]`
- You need to use a lambda to compare each x element to the new element in the list

### WIR
- I understood that we can only concatenate list objects, which helped with process of elimination 
- I understood we need to return a base case of []
- I understood we use recursion 

### Moral
- `.filter(f, iter)` returns an iterator object that can be called with `next(t) `
    - it is a lazy generator 
    - it expects an iterator passed in 
- Recursion bubbles back up from the base case 

</details>


<details><summary>Classes</summary>

<div class='tnr'>

Implement the Domino class. A Domino instance is constructed from a two-element list of non-negative integers below 10 that is stored as an instance attribute `ns`. The `align` method takes an integer first
which must be one of the numbers in `ns`. It returns the same domino **instance** on which it was **invoked**, but first mutates it so that first comes first in ns. A Domino([3, 4]) is displayed as 3-4.

</div>


```python
class Domino:
    """ Domino has two numbers and can be aligned to place one of them first.

    >>> d = Domino([3, 4])
    >>> original = d
    >>> d.align(3)
    3-4
    >>> d.align(4)
    4-3
    >>> d is original  # No new Domino instance was created
    True
    >>> d              # Domino's order is changed by align
    4-3
    """
    def __init__(self, ns):
        assert len(ns) == 2 and ns[0] in range(10) and ns[1] in range(10)
        self.ns = ns

    def align(self, first): 
        assert ______, 'first must be a number on the domino.'   # first in self.ns
        if ______:   # first != self.ns[0]:
            ______ # self.ns = [self.ns[1], self.ns[0]]
        return ______ # self 

    def __repr__(self):
        return ______
```

### WIW 
- By process of elimination I understood that we needed to check the element, I just chose two options:
    - `self.first == self.ns[0] or self.ns[1]`
        - this returns True or False, and it will always return True unless the item is 0. 
        - `self.first` is not a part of the instance attribute so this would error
    - `self.first in self.ns`
    - The comment 'first must be a number on the domino' $\implies$ that the number MUST be in the list without giving away the answer. 
- For the second blank, I correctly understood that we have a conditional check if the first passed in is not equal to the first index of self.ns, then we execute the clause. However I incorrectly chose `self.first != self.ns[0]`
- For the `if` clause I wrote `self.ns[1] = self.ns[:1] and self.ns[0] = self.first`
    - this statement is wrong, since it is checking the boolean value. 
    - Furthermore, `self.ns[:1]` would just return the 0th index, leading to the same problem that we were trying to solve for (i.e. flip it)
- For the return statement; by process of elimination I understood that the other recursive class classes calls did not make sense. I knew we had to return the `self`. However I chose option `repr(self.ns)`. This is wrong because we want to return the instance object, but also want it to be human readable, which is already what the next line `def __repr__(self):` is handling. On top of that, we aren't trying to return the list, we want it in a specific human readable format compared to the list of `self.ns`

### Moral
- the problem statement wants us to mutate the object in place. Python objects can be mutable. 
- we return `self` to allow for method chaining, common in OOP when you want to return a modified instance
- without `repr`, we would get a memory address instead of a human readable address

**New Vocab:**
- Method chaining in Python is a style of programming where multiple methods are called sequentially on the same object in a single statement.
- This is achieved by having each method return the object itself (usually by returning self)
- Allowing subsequent methods to be called directly on the result. It enhances code readability and conciseness, especially when performing a series of operations on an object.


#

**_list comprehension_**
<div class='tnr'>

Implement drop, which takes a Domino instance **d** and a list of **Domino** instances **ds**. It returns a new list with all of the elements of **ds** except for **d**.
</div>


```python
def drop(d, ds):
    """Return a new list of dominos with all elements of ds except d.

    >>> ds = [Domino(ns) for ns in [[5, 2], [3, 4], [5, 5], [3, 4]]]
    >>> drop(ds[1], ds)
    [5-2, 5-5, 3-4]
    >>> drop(ds[3], ds)
    [5-2, 3-4, 5-5]
    >>> ds
    [5-2, 3-4, 5-5, 3-4]
    """ 
    return __________ # [x for x in ds if x is not d]
```
<div class='tnr'>
What is the value of `drop(ds[2], drop(ds[1].align(4), ds))` assuming drop and Domino are defined correctly and ds is assigned to:
`ds = [Domino(ns) for ns in [[5, 2], [3, 4], [5, 5], [4, 3]]]`

<details><summary>Options</summary>

- [5-2]
- [5-2, 3-4]
- [5-2, 4-3]
- [5-2, 5-5]
- [5-2, 3-4, 5-5]
- [5-2, 4-3, 5-5]
- [5-2, 5-5, 4-3]
- [5-2, 3-4, 5-5, 4-3]
</details>
</div>

### WIW
- I filled in the blank with `ds[:].pop(d)`
    - I thought by new list it meant we can make a copy of the list and pop the element in it
- I almost chose the correct option, but I chose `[5-2, 3-4]`, the correct answer is `[5-2, 4-3]`
    - When retracing environment diagram, the only conclusion that would preserve `[5-2, 4-3]` is the fact that when we call `.align(4)` on that instance, we still are calling the function `drop` on that index 1, and we preserve the other instance that matches it 

### Moral 
- `list.pop()` takes an **index**, not a _value_
    - So `pop(d)` will raise a TypeError
- `[x for x in ds if x is not d]` keeps only the elements that do not refer to the exact same object as d.
- We can mutate objects in place, and we only remove the object instance.
    - `ds[1]` is the same object as `3-4`, but calling `.align(4)` on it mutates it in-place to `4-3`
    - ds[1] and ds[3] are now both 4-3, but they are different objects.
- Understand the difference between: 
    - `==` (value equality)
    - `is` (identity / same object)


#

<div class='tnr'>

Definition: A line of Dominos is a sequence of dominos in which pairs of adjacent numbers on different dominos are equal, such as `2-4 4-3 3-3 3-6`. Implement longest, which takes a list of Domino instances ds. It returns a string that describes the longest line of dominos that can be formed from `ds`. This result should contain domino repr strings separated by spaces, such as `'2-4 4-3 3-3 3-6'`. The dominos described in the result can appear in any order and may be flipped using the align method. If more than one line is longest, describe any of the longest lines. You may call **drop**.
</div>

```python
def longest(ds):
    """Return a string describing the longest line that can be formed from dominos in ds.

    >>> ds = [Domino(ns) for ns in [[5, 2], [3, 4], [5, 5], [6, 1], [3, 2]]]
    >>> print(longest(ds))
    4-3 3-2 2-5 5-5

    >>> ds = [Domino(ns) for ns in [[1, 2], [1, 2], [3, 2], [3, 2], [3, 2], [3, 2], [4, 3], [4, 3], [4, 3], [6, 5]]
    >>> print(longest(ds))
    2-1 1-2 2-3 3-2 2-3 3-4 4-3 3-4
    """
    def finish(first, rest):
        #   repr(first)         # d.align(first.ns[1]), drop(d, rest) first.ns[1] in d.ns
        s = [ ____ + ' ' + finish(____, ____) for d in rest if ____] 
        if not s:
            return ____ # repr(first)
                                # len
        return max(s, key=____) # must match for both options including max

    candidates = []
    for first in ds:
        candidates.append(finish (first,     drop(first, ds))) # left blank intentionally
        candidates.append(finish(first.align(first.ns[1]), drop(first, ds)))   # len
    return max(candidates, key=____)

```

### WIW
- I chose `repr(rest[0])` as first blank. It wouldn't make sense to index the rest in hindsight, I just dont know what `rest[0]` is pointing to. Is it the object instances in the list? and if so, how does repr(first) capture the first object instances in the list and we do a list comprehension for the rest of it? 
- We call `d.align(first.ns[1])` to find the max chain of domino sequences. 

### Walkthrough 
- `max(iterable_or_argument key=keyfunc)`
    - The `key=` argument lets you specify a function that transforms each element before comparing them.
    - If multiple items are maximal, the function returns the first one encountered.
- We want to make the first parameter wrapped in `repr` 
- We call the align method to mutate that object instance to see if it matches the 1-nth index object for the next call, and we drop the previously computed d to not work with the same list of object references again. 
- the `if ____ `part ensures we're only including the dominos in rest that can be aligned (i.e., where `first.ns[1]` matches `d.ns[0]` _after_ alignment).
- if our s is a false value (i.e. none; an empty list), then we return the repr of first (that Domino object itself)
    - Blank (k): repr(first) — If no further dominos can be added, we return repr(first) to indicate that the chain ends here.
- Lastly, we return the max character string. I got this wrong because I got tripped up on the comment about returning the numbers on a domino below 10. 

</details>

<details><summary>SQL</summary>

<div class='tnr'>
The Domino table has one row per domino that gives its unique id (number) and the numbers appearing on the domino m and n (numbers).
</div>

```sql
CREATE TABLE dominos AS
    SELECT 0 AS id, 3 AS m, 2 AS n UNION
    SELECT 1 , 3 , 1 UNION
    SELECT 2 , 6 , 3 UNION
    SELECT 3 , 4 , 4 UNION
    SELECT 4 , 3 , 2 UNION
    SELECT 5 , 2 , 6;
```

<div class='tnr'>
Complete this query that creates one row per domino for which at least one other domino has a number equal to its n value. The row contains the domino’s id, m value, n value, and the count of other dominos that have a number equal to its n value.
</div>

```sql
SELECT a.id, a.m, a.n, COUNT(*) FROM dominos AS a, dominos AS b
    WHERE _______ AND (_______)
    GROUP BY _______;
```

<details><summary>Options</summary>

i. (1.0 pt) Fill in blank (o).
- a.id = b.id
- a.id < b.id
- a.id != b.id

ii. (2.0 pt) Fill in blank (p).
- a.m = b.m OR a.n = b.n
- a.m = b.m AND a.n = b.n
- a.n = b.m OR a.n = b.n
- a.n = b.m AND a.n = b.n
- a.m = b.n OR a.n = b.n
- a.m = b.n AND a.n = b.n

iii. (1.0 pt) Fill in blank (q).
- m
- a.m
- b.m
- id
- a.id
- b.id
</details>

### WIR
- I understood that we dont want to `WHERE` on a table that has matching `.ids` because that would give a huge table, based on incorrect filtering. It wouldn't make sense to check which is greater as well. So we check for each `.id` incrementally by making sure the `.ids` are not the same when we perform an inner join
    -  So, using `a.id != b.id` ensures that we're comparing different dominoes
- We want to `GROUP BY` the `a.id` because we want the domino id per row 
    - grouping by `a.id` is important here because you're looking for the count of dominoes that have a number equal to the n value of the domino with the specific `a.id`. This means for each domino (as represented by its id), you want to count how many other dominoes have the same number on their m or n position. 
    - Grouping by `a.id` ensures that the results correspond to each domino individually.
        - **Why group by a.id and not b.id or id?**
            - Because we're analyzing each domino a, counting how many other dominoes b match its n value. Grouping by a.id gives us one row per original domino.
### WIW
- I thought we had to filter for `AND` to have both true cases, but we only needed to check with an `OR` to have more flexibility by comparing the number at the second position of domino a (a.n) with both positions of domino b.
- This condition ensures that any matching number will result in a valid pair, regardless of the orientation of the dominos.
</details>


<Details><summary>Link Class and Generators</summary>
<div class='tnr'>

Implement repeat, a generator function that takes a non-empty finite linked list s and a positive integer k. It yields k elements from s, restarting from the first element of s each time the end is reached. It is ok to mutate s. You may call cycle.
</div>

```python
def repeat(s, k):
    """Yield k items from a non-empty finite linked list, starting over as needed.
    It is ok to mutate s in the process.
    >>> t = repeat(Link(4, Link(2, Link(6))), 10)
    >>> [next(t), next(t), next(t), next(t)]
    [4, 2, 6, 4]
    >>> list(t) # 6 of the 10 elements remain
    [2, 6, 4, 2, 6, 4]
    """
    for x in _______: # range(k):
        yield _______ # s.first 
        _______ # s = cycle(s)
```

### WIR 
- I got options 1 and 3 right. 

### Hindsight
- I first chose `from repeat(s.rest, k-1)`
- What I want to understand is how the recursive list is preserved and we are able to call s.first at each iteration of the lazy generator
- `repeat` is a generator function. That means when you call it, you get back a **generator object** that keeps its own internal state across calls to `next()`
- It doesn't cycle the list.
- It restarts the generator each time.
- It creates a new generator object per recursive call, defeating the purpose of lazy iteration
- `cycle(s)` is only called once — at the beginning — to mutate the list into a circular one. After that, we never call cycle again
    - You call `cycle(s)` once to mutate the list into a cycle.
    - The generator function has a local variable s that moves forward in the cycle with each `next()`.
    - The generator object retains s's current position in memory, thanks to Python's generator state model.

### Moral:
- The generator function can keep track of object attributes when you call next(t) on them. 
- This means you don't need recursion as it handles it self when looping through the instance.

</details>


<details><summary>Trees</summary>
<div class='tnr'>
Implement count_ones, which takes a Tree instance t. It returns the number of nodes in t that have one child. The Tree class is defined on Page 2 of the Midterm 2 study guide.
</div>

```python
def count_ones(t):
    """Return the number of nodes that have one child.
    >>> count_ones(Tree(1, [Tree(2), Tree(3, [Tree(4)])]))
    1
    >>> count_ones(Tree(1, [Tree(2), Tree(3), Tree(4)]))
    0
    >>> count_ones(Tree(1, [Tree(2, [Tree(3, [Tree(4)]), Tree(5, [Tree(6)])])]))
    3
    """
    count = sum([ count_ones(_______) for b in t.branches if _______ ])
    if _______:
        return count + 1
    else:
        return count
```

Options: 

(1.0 pt) Fill in blank (a).
```
    b
    t
    b.branches
    t.branches
```
ii. (1.0 pt) Fill in blank (b).
```
    True
    is_leaf(b)
    is_leaf(t)
    len(b.branches) == 1
    len(t.branches) == 1
```
iii. (2.0 pt) Fill in blank (c).
```
    True
    is_leaf(b)
    is_leaf(t)
    len(b.branches) == 1
    len(t.branches) == 1
    all([len(b.branches) == 1 for b in t.branches])
    any([len(b.branches) == 1 for b in])
```
### Moral: 
- When you have one branch, it implies that it has a own node that is a leaf. 

#

<div class='tnr'>
Implement shorten, which takes a Tree instance t. It removes all non-root nodes that have no siblings (no other nodes with the same parent), then returns t.
</div>

```python
def shorten(t):
    """Remove all non-root nodes with no siblings and return t.
    >>> shorten(Tree(1, [Tree(2), Tree(3, [Tree(4)])]))
    Tree(1, [Tree(2), Tree(3)])
    >>> shorten(Tree(1, [Tree(2, [Tree(3, [Tree(4)])])]))
    Tree(1)
    >>> shorten(Tree(1, [Tree(2, [Tree(3), Tree(4)])]))
    Tree(1, [Tree(3), Tree(4)])
    >>> shorten(Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])]))
    Tree(1, [Tree(3, [Tree(4), Tree(5)]), Tree(6)])
    """
    _______: # while len(t.branches) == 1
        _______ = _______ # t.branches = t.branches[0].branches
    for b in t.branches:
        shorten(b)
    return t
```

### WIW

Why other options for second blank are wrong: 

    t
    t.branches[i]
    Tree(t.label, t.branches)

`t`
-  This changes t to a list `(t.branches[0].branches is a list)`, not a Tree.
- t was originally a Tree instance; replacing it with a list breaks the structure.
- Later code `(for b in t.branches:)` assumes t is still a Tree. That would raise an error like AttributeError: 'list' object has no attribute 'branches'.

`t.branches[i]`
- This tries to assign a list of branches (e.g., [Tree(3)]) to a single element in the list (t.branches[i], or t.branches[0]).

`Tree(t.label, t.branches) = t.branches[0].branches`
- You can’t assign to a constructor call like Tree(...) — this is a syntax error in Python.
- The left-hand side is not a variable; it's an expression that creates a new object.
- Even if you could assign to it, it doesn't change the original tree t at all.
- Also, Tree(...) = ... doesn’t make any sense — you’re not assigning to anything mutable

### Moral:
- Garbage collection in Python is an automated memory management process that deletes objects when they are no longer in use.
    - it does this by counting the references and ones that are unused
- When we set the `len(t.branches) == 1`, we check for where there are branches that have no siblings
- Then, we bind `t.branches` to be a list of that node (i.e. a reference pointer to there)
- We exit the while loop, loosing the reference due to garbage collector, and recursively call `shorten(b)` on every branch left. When its not true, we return the new `t` 

#

<div class='tnr'>

What order of growth describes the time it takes to execute `u = Tree(1, [t])` in terms of the number of nodes in a Tree instance `t`. Assume every non-leaf node in `t` has two children.

Options: 

    constant
    logarithmic
    linear
    quadratic
    exponential
</div>

### Moral: 
- Just pointer assignment → O(1) time.
- You're not modifying or inspecting t — you're just wrapping it inside a new Tree. So it's constant time, regardless of how big t is.
- Creating a new tree that points to an existing tree is constant time. Traversing or modifying the tree is not.
</details>


<details><summary>Scheme</summary>

<div class='tnr'>

A nested list of numbers is a list containing numbers and nested lists of numbers. For example: `((7 5) 3 ((1)) 9)`
Implement truths, which takes a nested list of numbers s and a one-argument procedure f. It returns the count of numbers x in s for which (f x) returns a true value.

```scm
scm> (define (eight? x) (and (number? x) (= x 8)))
scm> (truths '(8 (8 ((3 8)) 8 ())) eight?)
4
scm> (truths '(8 (8 ((3 8)) 8 ())) number?)
5
Hint: The built-in number? procedure returns whether its argument is a number.
```
</div>

```scm
(define (truths s f)
#| 
scm> (define (eight? x) (and (number? x) (= x 8)))
scm> (truths '(8 (8 ((3 8)) 8 ())) eight?)
4
scm> (truths '(8 (8 ((3 8)) 8 ())) number?)
5
|#

(if (null? s) 0
    (+
    (if (number? (car s)) _______ (truths _______ f)) ; first argument to +
    _______ ))) ; second argument to +


(define (truths s f)
(if (null? s) 0
    (+
    (if (number? (car s)) (f (car s)) (truths (cdr s) f)) ; first argument to +
    (truths (cdr s) f) ))) ; second argument to +
```

### Moral: 
- Divide-and-conquer approach:
    - Break off the first item (car s)
    - If it’s a number → test it
    - If it’s a list → recurse into it
    - Then move on to the rest (cdr s)

</details>