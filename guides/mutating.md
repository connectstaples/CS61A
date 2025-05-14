#### CS61A Sp25 Prof Denero
# Mutation v.s. Non-Mutation
#### Sean Villegas

## Things That *Do* Mutate the Global Frame

- `global var` followed by assignment:
```python

lst = [1, 2, 3]

def change():
    global lst
    lst = [9, 9, 9]  #  full reassignment

change()

print(lst)  # → [9, 9, 9]

```
## List Mutations

```python

lst = [1, 2]

def mutate_lst(): 
    lst.append(4) # [1, 2, 4] # adding brackets will make it a sub list

    lst.extend([5, 6, 8]) # [1, 2, 5, 6, 8] # adding extra brackets will make it a sub list

    lst.insert(1, 99) # [1, 99, 5, 6, 8]

    lst.pop() / lst.pop(0) # 8 / 1 = 8.0 # lst is now [99, 5, 6]

    lst.remove(5) # [99, 6]

    lst[0] = 999 # [999, 6]

    del lst[1] # [999]

    lst[:] = [7, 8, 9]  # (slice assignment reassigned the whole thing [:] usually makes a copy) [7, 8, 9]

    lst.sort() # (in-place) # [7, 8, 9]

    lst.reverse() # [9, 8, 7]

    # lst.clear() # would clear whole lst making it empty and a false value
mutate_lst()  # final output is an updated lst of [9, 8, 7]

```
## Dictionary Mutations

```python

d = {"a": 1, "b": 2, "c": 3}

# 1. Add or update items
d["d"] = 4   # Add new key
d["a"] = 10  # Update existing key
d.update(e=5) # Add using keyword argument
d.update({"f": 6}) # Add using another dict

# 2. Remove items
d.pop("b")  # Remove key 'b'
del d["c"]  # Remove key 'c' using del
d.popitem() # Remove last inserted item (Python 3.7+)
# At this point, 'f' is the last item, so it's removed

# 3. Conditionally add (only if key doesn't exist)
d.setdefault("g", 7)  # Adds 'g' with value 7
d.setdefault("g", 999)  # Does **NOT** overwrite existing 'g'

# 4. Modify values
d["d"] += 1  # Increment value of 'd'

# 5. Clear all items
# d.clear() # Removes everything from the dict

print(d)  # Output: {}

```
- you must always specify the key to be removed from a dictionary when using the `pop()` method.

## Set Mutations
- `s.add(x)`
- `s.remove(x)`
- `s.discard(x)`
- `s.update(...)`
- `s.clear()`

## Function-Induced Mutations
- Passing a global mutable object to a function that mutates it:
  - `mutate(nums)` where `def mutate(lst): lst.append(999)`

## Other Global State Mutations
- Mutating a shared/global object’s attributes:
  - `config.debug = True` *(if `config` is global)*
- Writing to files, databases, or external systems
- Using `nonlocal` to mutate a variable in an enclosing (non-global) scope

---

## Things That *Do Not* Mutate the Global Frame

## Safe Reads and Copies
- Reading from a global variable: `x = nums[0]`
- Iterating over a global list: `for x in nums: ...`
- Calling `list(nums)` *(creates a shallow copy)*
- Using list slicing for a copy: `nums[:]`, `nums[1:3]`
- Using comprehensions: `[x + 1 for x in nums]`
- Using `map`, `filter`, `sorted`, etc.:
  - `map(f, nums)`
  - `filter(f, nums)`
  - `sorted(nums)`
- Generator expressions and iteration:
  - `(x for x in nums if x > 0)`

## Local-Only Changes
- Reassigning a *local* variable with the same name:
  - Inside a function: `nums = [0]` *(local scope only)*
- Returning a new list: `return nums + [1]`
- Accessing attributes or properties:
  - `len(nums)`, `sum(nums)`, `min(nums)`, etc.

