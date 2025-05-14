## Takeaways

**Accessing Class Instance Attributes**
- A mistake I made is thinking that to access an instance attribute in between two different classes, I must call it by its Class **object** name. In reality, depending on the instance attribute you must use the lowercase that is defined. Static variables are class attributes, and instance variables are changing
e.g. 
```python
class Valet:
    def __init__(self):
        self.tips = 0 
        self.garage = None
    def park(self, car):
        self.garage.cars[car] = self # notice how garage is lowercase 

class Garage:
    def __init__(self, valets):
        self.cars = {}
        for valet in valets:
            valet.garage = self
```

**Generators**
- `Yield from` executes a list to exhaustion, `Yield` is a lazy generator 
- In order for an **iterator** to be evaluated, it must be initialized as an **iterable**. thus we must use a generator function to allow for iteration.
- Iterators in python:
    - `iter` # initialize 
    - `yield from` # initialize 
    - `yield` # initialize 
    - `next` # initialize

**Link Class**:
- Every instance of the Class `Link` will have a Link.empty 
- Pay attention to the skeleton code has a **base case** 

**Overriding**:
Use `super().method_name(args)` to call the **parent’s version**, then add your own logic to override or extend it.

```python
class SubClass(ParentClass):
    def method_name(self, param1, param2, ...):
        # Call the parent class's method (optional)
        result = super().method_name(param1, param2, ...)
        # Add subclass-specific behavior
        # (e.g., modify result, add new steps)
        return result  # or whatever the method should return
```
- Overriding: When a subclass defines a method with the same name and signature (parameters) as a method in its parent class, it overrides the parent’s version. The subclass’s version is called instead of the parent’s when invoked on an instance of the subclass.

**List comprehension with condition:**
```python
[expression for variable in iterable if condition]

```
- A pattern you may see, is observing the pointers in a list comprehension. `<expression>` is an instance attribute, that is a **object** with **pointer** within a _list_ previously defined  

**Constructor:**
- A constructor in Python is the `__init__` method, which initializes a new instance of a class.

**Inheritance:**
- The `super()` function calls a method (like `__init__`) from the parent class of a subclass.

**The overriden constructor:**
- In Python, when a subclass defines its own `__init__ method`, it overrides the parent class’s `__init__` method.
- This means the subclass’s `__init__` takes over as the constructor called when a new **sub class** instance is created. 
    - However, the **subclass** can still call the parent’s `__init__ `using `super()` to _reuse_ its functionality. 

**Truthy If Statement Evaluation:**
```python
if <variable>:
    # Do something when <variable> is truthy
    return <variable>

if <variable> not in <iterable>:
    # Suite executes if <expression> is not present in <iterable>
    return <variable>
```

**Implicitly Returning None in Functions with `if`, `for` or `while` Statements** 
```python
"""
If the statement evaluates to Truth, then it will `not` be Truth. Thus it will not execute the suite. When a for statement, if, or while statement does not execute the suite its enclosing function will **implicitly** return `None`
"""
if <variable> not in <iterable>:
    # Suite executes if <expression> is not present in <iterable>
    return <variable>
```
- in python if a function doesn't return a value (i.e. it reaches the end of a program without executing a return statement) it automatically returns `None`
## Question 1

**Complete the class Item so the docstrings pass**

Notes:
- recognize the data types in the docstring when you call their attributes

```python

class Item:
    """
    >>> broccoli = Item("broccoli", 1, "veggies")
    >>> broccoli.name
    'broccoli'
    >>> broccoli.quantity
    1
    >>> broccoli.category
    'veggies'
    >>> broccoli
    Item("broccoli", 1, "veggies")
    """

    def __init__(self, name, quantity, category):
        self.name = name
        self.quantity = quantity
        self.category = category

    def __repr__(self):
        _____________
```
Answer to match datatypes: 
```python
        return f"Item('{self.name}', {self.quantity}, '{self.category}')"
```

## Question 2
Each instance of `GroceryList` has instance variables tracking the `store_name` and `items` (a list of `Item` instances)

```python
class GroceryList:
    def __init__(self, store_name):
        self.store_name = store_name 
        self.items = []

    def add_new_item(self, name, quantity, category):
        """Creates new Item with provided name, quantity, category. 
        Adds new item to lists items and returns it. If item with that name 
        exists, it returns None"""

                            # access item name for _ in the instance attribute of self.items
        existing_item_names = [item.name for item in self.items]
            # if the _ not in our variable list 
        if name not in existing_item_names:
                        # you call the Item class with parameters from add_new_item
            new_item = Item(name, quantity, category)
                    # append to self.items with our new_item variable 
            self.items.append(new_item) 
            return new_item # return the new item 
        
    def all_for_category(self, category): 
        """Returns list of all items for given category"""
        # return the item variable for item variable in the instance attribute of items iterable if the item instance variable equals the category for the function 
        return [item for item in self.items if item.category == category]
```

`GroceryList` class has two methods 
- **add_new_item** which adds new items to `items` if they dont exist 
- **all_for_category** which returns all the items for a given `category`


Notes:
- **all_for_category** 
    - return with list comprehension the `category` in `existing_item_names` 
- **for loops** do not need to return a value unless the function logic is needed 
- Within **list comprehensions** you can alter the names e.g.:
```python
# item
existing_item_names = [item.name for item in self.items]

# items
existing_item_names = [items.name for items in self.items]
```
- `append()` will add the variable to the end of the list 
- Parameter name example
```python
# item
return [item for item in self.items if item.category == category]

# items
return [items for items in self.items if items.category == category]
```

## Question 3
`SharableList` is a class that inherits from `GroceryList` class. It allows a shopping list to be shared by multiple users. Each instance of `SharableList` has same instance variables as `GroceryList` (**store_name** and **items**) but also has two additional instance variables 

```python
class SharableList(GroceryList):
    """
    >>> roomie_list = SharableList('Trader Joes', ['don@key.com', 'star@burns.com'])
    >>> roomie_list.store_name
    'Trader Joes'
    >>> roomie_list.items
    []
    >>> roomie_list.collaborators
    ['don@key.com', 'star@burns.com']
    >>> roomie_list.items_by_adder
    {'don@key.com': [], 'star@burns.com': []}
    >>> roomie_list.add_new_item('Wasabi Peas', 100, 'snacks', 'don@key.com')
    Item('Wasabi Peas', 100, 'snacks')
    >>> roomie_list.items_by_adder
    {'don@key.com': [Item('Wasabi Peas', 100, 'snacks')], 'star@burns.com': []}
    """
        def __init__(self, store_name, collaborators):
            __________
            self.collaborators = collaborators
            self.items_by_adder = {_____ for _____}

        def add_new_item(self, name, quantity, category, adder):
            new_item = __________
            if new_item:
                __________
            return new_item

        def __init__(self, store_name, collaborators):
# super().__init__(store_name) calls the parent class (GroceryList) constructor (__init__) and passes the store_name parameter to initialize it, allowing SharableList to extend that initialization.          
            super().__init__(store_name)
            # extend 
            self.collaborators = collaborators 
# key: value for the name in instance attribute of collaborators 
            # extend
            self.items_by_adder = {collaborator: [] for collaborator in self.collaborators}

# overriding and extending example
        def add_new_item(self, name, quantity, category, adder):
# use the parent class method with parameters 
            new_item = super().add_new_item(name, quantity, category)
            if new_item:
                self.items_by_adder[adder].append(new_item)
            return new_item
```
- **collaborators** is a list of email addresses, created when constructing an instance 
- **items_by_adder** is a dictionary tracking which email address added which item. Starts off as dictionary with key for each email address mapped to an empty list 

To support tracking who added what, `ShareableList` overrides `add_new_item` method so that it calls original method but then updates `items_by_adder` accordingly 

Notes:
- A constructor in Python is the `__init__` method, which initializes a new instance of a class.
- The super() function calls a method (like `__init__`) from the parent class of a subclass.

Question: 
- Which func overrides the parent class?
    - Answer: `add_new_item`

## Question 4 
- _uses link class_
- Implement `product`, a function that takes in a  linked list `s` and returns the `product` over all the values in the linked list. Assume that the initial list `s` is not `Link.empty`

```python
def product(s):
    """
    Takes in a linked list S and returns the product over all the values in the  linked list

    >>> product(Link(2, Link(5))) # 2 * 5 = 10 
    10 
    >>> product(Link(2, Link(7))) # 2 * 7 = 14
    14
    >>> product(Link(7, Link(2, Link(7)))) # 7 * 2 * 7 
    98
    >>> product(Link(5))
    5
    """

    if s is Link.empty:
        return 1 
    return s.first * product(s.rest)

```

Notes:
- `product` is updating based on `s.rest` at the recursive call 
- we have a base case, hint to use recursion 
- Question: Why do we return 1, is it because there is only one element, s.first? Why wouldn't we do `return s.first`?
    - Answer(s): 
        - We return 1 in product so that it will multiply 1 once we reach the end of the Link list, to not alter the values in the Link list
        - Every Link instance has a `self.rest` that eventually leads to `Link.empty` 
        - Even if we misinterpreted and meant “return s.first when there’s one element,” the base case isn’t about “one element **left”—it’s about no elements left (Link.empty).**
    
## Question 5
- 

```python
class Valet:
    """A valet is tipped after they wash a car, or after one of their parked cars is washed.

    >>> shaun = Valet()
    >>> katy = Valet()
    >>> g = Garage([shaun, katy])
    >>> shaun.park('Benz')
    >>> katy.park('Benz')
    >>> shaun.wash('Benz', 1) # 1 dollar to shaun
    >>> katy.wash('Benz', 2) # 1 dollar to  katy & 1 to shaun

    >>> shaun.park('Rolls')
    >>> katy.park('Rolls')
    >>> katy.wash('BMW', 2) # 2 to katy
    >>> shaun.wash('Rolls', 2) # 1 to shaun & 1 to katy
    >>> [shaun.tips, katy.tips]
    [3.0, 4.0]
    """
    def __init__(self):
        self.tip = 0 
        self.garage = None
    def park(self, car):
       _____________
    def wash(self, car, tip):
        self.tips += tip / 2
        ________ += tip / 2 

class Garage:
    """A garage holds cars parked by valets who work there."""
    def __init__(self, valets):
        self.cars = {}
        for valet in valets:
            ________ = ________
```


## Question of Generators
An infinite Iterator `t` is one for which `next(t)` can be called any number of times and always returns a value.

Implement `ring`, a generator function that takes a non-empty list `s`. It returns an infinite generator that repeatedly yields the values of `s` in the order they appear in `s`. 

```python
def ring(s):
    """Yield all values of non-empty s in order, repeatedly.
    >>> t = ring([2, 5, 3])
    >>> [next(t), next(t), next(t), next(t), next(t), next(t), next(t)]
    """
    _________:
        _________
```
Notes: 
- In order for an **iterator** to be evaluated, it must be initialized as an **iterable**. thus we must use a generator function to allow for iteration. 
- My first thought was to use `iter` func. However, we know that `iter` only allows for iteration once and it cannot be reused. This wouldn't fullfill the infinite generator requirement
- `While True` creates an infinite loop because all values in python are **True** besides 0, None, and some Error that could throw the loop off. 
- `Yield from` executes a list to exhaustion, `Yield` is a lazy generator 

```python
def ring(s):
    """Yield all values of non-empty s in order, repeatedly.
    >>> t = ring([2, 5, 3])
    >>> [next(t), next(t), next(t), next(t), next(t), next(t), next(t)]
    """
    # Attempt 1
    while True:
        next(iter(s)) 

    # Attempt 2 
    while True:
        yield from s
```

## WWPD Question
| Expression | Interactive Output |
| ------- | ------ | 
| pow(10, 2) | 100 | 
| print(4, 5) + 1  | 4 5<br>Error | 
|  [m.x, n.x] | `['ei', 'um']` # C.x is now 'eo' | 
| [C.f(n, 'a').x, C().x] |  | 
| print(m, n) |  | 
| n |  | 
| g([3, 4, 5]) |  | 
| py[3][5] | `[7]` | 
| code | `[3, 4, 3, [4]]` | 

```python 
class C:
    x = 'e'
    def f(self, y):
        self.x = self.x + y
        return self
    def __str__(self):
        return 'go'
class Big(C):
    x = 'u'
    def f(self, y):
        C.x = C.x + y
        return C.f(self, 'm')
    def __repr__(self):
        return '<bears>'
    m = C().f('i')
    n = Big().f('o')

def g(y):
    def h(x):
        nonlocal h
        k = 2
        if len(x) == 1:
            h = lambda x: y
            k = 1
        return [-x[0]] + h(x[k:])
    return h(y)

py = {3: {5: [7]}}
thon = {5: 6, 7: py}
thon[7][3] = thon
q = range(3, 5)
r = iter(q)
code = [next(r), next(iter(q)), list(r)]
```

Notes: 
- `nonlocal` keyword is used to work with **variables** inside nested functions, where the variable should not belong to the **inner** functions frame.
    - Use the keyword `nonlocal` to declare that the variable is ___**not local**___.\
E.g.
```python
def outerf():
    """
    >>> print(outerf())
    20 
    """
    x = 10 
    def innerf():
        nonlocal x 
        x = 20 
    innerf()
    return x 
```