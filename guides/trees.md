### Prof Denero, Sp25 CS61A
# Tree Class
##### Sean Villegas


[htdp online textbook in scheme](https://htdp.org/2018-01-06/Book/part_prologue.html)

<style>

    .tnr {
        font-family: "Times-New-Roman";
        font-size: 16px;
    }

    .ver {
        font-family: "Verdana";
        font-size: 16px;
    }

</style>

## Tree instance has two instance attributes:
 - `t.label` is the value stored at the root of the tree.
 - `t.branches` is a list of Tree **instances** that hold the labels in the rest of the tree.
- The Tree class (with its `__repr__` and `__str__` methods omitted) is defined as:
- On exam problems, draw out the tree always  

```python
class Tree:
    """A tree has a label and a list of branches.

    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
```

## For a tree:
- Its root label can be any value, and `t.label` evaluates to it.
    - The root label is always larger than all of its ancestors 
- Its branches are always `Tree` instances, and `t.branches` evaluates to the list of its branches.
- `t.is_leaf()` returns `True` if `t.branches` is **empty** and `False` otherwise.


## Displaying a tree:
- `repr(t)` returns a Python expression that evaluates to an equivalent tree.
- `str(t)` returns one line for each label indented once more than its parent with children below their parents.


## Mutating a tree:
- `t.label = y` changes the root label of t to y (any value).
- `t.branches = ns` changes the branches of t to ns (a list of Tree instances).
- Mutation of t.branches will change t.
    -  E.g. `t.branches.append(Tree(y))` will add a leaf labeled y as the right-most branch.
- Mutation of any select branch will change it.
    - E.g. `t.branches[0].label = y` will change the root label of the left-most branch to y.

```python
t.label = 3.0
t.branches[1].label = 5.0
t.branches.append(Tree(2, [Tree(6)]))
print(t)
"""
3.0
  1
    4
    1
  5.0
    9
  2
    6
"""
```

| Feature                      | Tree Constructor and Selector Functions | Tree Class |
|------------------------------|-----------------------------------------|-----------|
| **Constructing a tree**      | `tree(label, branches)` constructs a tree | `Tree(label, branches)` constructs a Tree object (calls `Tree.__init__`) |
| **Label and branches**       | `label(t)` gets the label, `branches(t)` gets the branches | `t.label` gets the label, `t.branches` gets the branches |
| **Mutability**               | Immutable (cannot assign values to call expressions) | Mutable (`t.label` and `t.branches` can be reassigned) |
| **Checking if a tree is a leaf** | `is_leaf(t)`  | 



## _Solving Tree Problems Lecture_ 
<div class="tnr">

Implement **bigs**, which takes a Tree instance t containing integer labels. It returns the number of nodes in t whose labels are larger than any labels of their ancestor nodes. 

Tree drawing: 

```
    1 # root 
        4 # Tree instance
            4 # children
            5
        3
            0 # children 
            2
```
```python
def bigs(t):
    """Return number of nodes in t that are larger than all their ancestors
    
    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(a)
    4

    def f(a, x):
        if t.label > t.branches:
            return 1 + _______

        else: 
            return _______
        return _______
    """
```

</div>


<div class="ver">

<details>
<summary>Notes on problem and how to attack</summary>


1. In this problem and similar, we can see that there is a helper function with a base case for recursion, that accepts 2 arguments
2. We need to keep track of the `node.label` and compare it to the max ancestor label in the tree
    - since the root label is always larger than all of its ancestors you need to decrement it down to start the chain of processes  

</div>

```python
def bigs(t):
    """Return number of nodes in t that are larger than all their ancestors
    
    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(a)
    4

    def f(a, x):
        if t.label > t.branches:
            return 1 + sum([f(b, a.label) for b in a.branches])
        else: 
            return sum([f(b, x) for b in a.branches])
        return f(t, t.label - 1)
    """
```

</details>


## Recursive Accumulation 
- specification is same, but the implementation is different, i.e. we append the result of the sum into a `counter`

```python
def bigs(t):
    """Return number of nodes in t that are larger than all their ancestors
    
    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(a)
    4

    def f(a, x):
        n = [0]

        if _________:
            _________
        _________:
            f(_________) 
    _________
    _________
    """
```


### Q3 
<div class="tnr">
Implement smalls, which takes a Tree instance t containing integer labels. It returns the non-leaf nodes in t whose labels are smaller than any labels of their descendant nodes. 
</div>

```python
def smalls(t):
    """Return the non leaf nodes in t that are smaller than all their descendants
    
    >>> a = Tree(1, [Tree (2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]
    """

    result = []
    def process(t):
        if t.is_leaf(): 
            return __________
        else:
            smallest = __________
            if __________:
                __________
            return min(smallest, t.label)
    process(t)
    return result

```
</div>



<div class="ver">
<details>
<summary>Notes</summary>

Idea:
- For every node, check if it is a leaf, if it is, you hit a base case and return its .label 
- Check if this label is smaller than all of its ancestors _everywhere_ 
append the labels to `result`

```python
def smalls(t):
    """Return the non leaf nodes in t that are smaller than all their descendants
    
    >>> a = Tree(1, [Tree (2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]
    """

    result = []
    def process(t):
        if t.is_leaf(): 
            return t.label
        else:
            smallest = min([process(b) for b in t.branches]) # minimization through list comprehension and recursion 
            if t.label < smallest:
                result.append(t)
            return min(smallest, t.label)
    process(t)
    return result
```

</details>

<div>