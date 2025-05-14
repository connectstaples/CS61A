#### CS61A Sp25 HW07
# Scheme
#### Sean Villegas


Rules to live by: 
- prefix notation always when evaluating expressions
- evaluating expressions requires parenthesis around it 


**Question** Implement a procedure `pow` that raises a number `base` to the power of a nonnegative integer `exp`. The number of **recursive** pow calls should grow logarithmically with respect to exp, rather than linearly. For example, (pow 2 32) should result in 5 recursive pow calls rather than 32 recursive pow calls.

- `cond` is already `if elif else` logic
- `cond` doesnt use if explicitly unlike using if 
    - **note**: `if` in scheme is usually for if else (only two scenarios). `cond` allows for more 
    - normal `if` statements already have else defined as fallback
- `even` and `odd` return a boolean value `#t` or `#f`
    - scheme uses that boolean value to determine which branch or clause to execute 


- **only** `cond` allows you to use `else` 
- Using even: 
    ```scheme
    (define (even_or_not x) 
        (if (even? x)
            (display "is even\n")
            (display "odd")
        )
    )
    ```
<center>Translate from python</center>

```python
def pow(base, exp):
  """
  Calculates base raised to the power of exp using recursion,
  with the number of recursive calls growing logarithmically with respect to exp.
  """
  if exp == 0:
    return 1
  if exp == 1:
    return base
  if exp % 2 == 0:  # even
    return pow(base * base, exp // 2)  # Square the base and halve the exponent
  else:             # odd
    return base * pow(base * base, (exp - 1) // 2)  # Square the base, halve the exponent, and multiply by base
```

```scheme
(define (square x) (lambda (x) (* x x)))

(define (pow base exp)
    (cond
        ((= exp 0) 1)
        ((= exp 1) base)
        ((even? exp) (pow (square base) (/ exp 2)))
        ((odd? exp) (* base (pow (square base) (/ (- exp 1) 2))))
    )
)
```

**Question** Implement repeatedly-cube, which receives a number x and cubes it n times.
```scheme
scm> (repeatedly-cube 100 1) ; 1 cubed 100 times is still 1
1
scm> (repeatedly-cube 2 2) ; (2^3)^3
512
scm> (repeatedly-cube 3 2) ; ((2^3)^3)^3
134217728

(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let
            (_________________)
            (* y y y))))

```

## **Question 3**

$$car{\implies} first$$
$$cdr{\implies} rest$$

1. If you call `cdr` on empty list it will create an error
2. `cdr` does not _need_ a car

$$Link.first{\implies} first$$
$$Link.restp{\implies} rest$$

## `cons`
- cons cell represents a list or pair values

```scheme
> (cons (cons 1 nil) (cons 2 nill))
((1) 2) 
```

## `list` 
- can be defined as: 
    - `nil` implying empty
    - or pair whose `cdr` is another list 

## **Control & Flow:**
- Special forms are syntax elements with special evaluation 

## **Rules:** 
- procedures evaluate arguments before applying procedure
- e.g. Special forms:
    - `if` a conditional eval 
    - `cond` multiple conditional eval 
    - `set!` variable assignment 
    - `delay` promise creation
    - `force` promise evaluation 
    - `quote` prevent evaluation 
    - `let`
    - `lambda`
    - `define` 
    - `length` 

## Stream Promise Concept 
- `car` and `cdr` are _stream promises_ 

`delay` evaluation: 
- object that represents a value that might not be computed yet 
- computation is lazy evaluation to save space in memory
- when accessing elements you force promise to get value, similar to the map call on an iterable 

`delay`: 
- special form `delay` creates a promise
- takes an expression as input and returns `promise object` which itself represents the future result of evaluating that expression

`force`:
- `force` takes promise as input 
- evaluates expression with promise and returns resulting value
- in memory, it is memoized in cache
