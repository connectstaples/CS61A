#### CS61A Final 24
# Environment Frames and Generators 
#### Sean Villegas


## Q.1a
```python
def cut(s):
    this = 1
    for x in s:
        if this:
            this = x
            yield this
        else:
    this = True
    
def paste(n):
    yield n
    for x in paste(n + 1):
        yield 2 * x
    yield n
def copy(t, k):
    return [next(t) for x in range(k)]

nums = [0, 2, 4, 6, 8]
```
Write the output that would be displayed by printing the result of each expression. If an error occurs, write
ERROR

### a. `list(cut(nums)) # output: [0, 4, 6, 8]`

**Remember**: 
- _every time a generator function encounters a `yield`, it yields current value and pauses_ 

- An `if <expression>` evaluates the boolean value
    - Therefore every iteration checks the truthy value

**Approach**: 
- `this` executes because its a truthy value i.e. `this = 1` 
- `this` becomes truthy in else statement, but will not yield the current binded `this`
    -  When the element is false, we assign this to Truthy and move on to the next element without capturing that false element 
        - which is due to the `else` statement
- `list` called on a yield generator will force computation to exhaustion 
- when we use num, it is a shallow reference, only reads from `nums`; doesn't update or mutate. Not accessible UNLESS saved by some variable. 



### b. `list(cut(map(lambda x: x - 4, cut(nums)))) # [-4, 0, 4]`

**Approach**: 
- Recall that list will make a lazy generator yield till exhaustion 
- evaluate inner procedures first
- apply nums to lambda
- finally evaluate the final cut 


### c. `copy(paste(0), 3)`

**Review for problems regarding depth**

- Notice that `paste` will yield infinitely unless you specify a range, which is what `copy` does 
- **Key concept: generators are paused, and don't "bubble" until forced**
    - bubble scenario: imagine a bunch of boxes wrapped up together, this is your nested for loops that compute values and _bubble_ back up 

- This function will yield a total of 3 times due to the list comprehension of `range(3)`. It will open its own frames and yield its own values, but we return to the depth 0 and compute the `yield 2 * n` **twice**, with the inner depth for loop values that are computed each time we recursively call `paste(n)`

```
[0, 2, 8] # values at depth 0 that `next()` generates with range of 3 
yield n (i.e. 0)

THEN for x in paste(n + 1)
| | --------  0 + 1 -> 
        in depth 1: yield 1 -----> depth 0 grabs 1 and finishes its for loop of 2 * 1 = 2 ----> (i.e. at depth 0 we have called next to generate that value)
THEN for x in paste(n + 1)
| | ------ 1 + 1 -> 
        in depth 2: yield ---> depth 0 grabs 2 and finishes its for loop of 2 * 2 = 4 ----> then we open depth 3 for loop of 
THEN for x in paste(n + 1)
| | ----- 2 + 1 -> 
        in depth 3: yield 3 ---> depth 0 grabs previous 4 and finishes its for loop of 2 * 4 = 8. Then we stop because we have hit our range

First value (from paste(0)): 0.
Second value (from paste(1)): 1 → 2 * 1 = 2.
Third value (from paste(2)): 2 → 2 * 2 = 4 → 2 * 4 = 8.
```



