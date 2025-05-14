#### Disc 13 Sp25; Apollo Loh
# Interpreters 
#### Sean Villegas

- It evaluates its arguments from left to right.
- everything in scheme can be represented in linked lists in python. 
    - in this case its pair; with `car` and `cdr`

## Link class in `python` and List Structure in `scheme`
- **note** that `Link.empty` is `nil` equivalent in scheme 
- Difference in nil and forming structures in python and scheme: 
    ```python
    >>> Link(0) # will automatically handle link.empty for us
    ```
    Scheme: 
    ```scm
    (Pair 0) ; will error - you need to have nil passed in when ending a list structure 
    ```

## `Scheme` Evaluation 
1. copy the whole pair (list) and subexpressions 
2. left to right
    - eval all symbols (besides parenthesis)
    - **DONT** evaluate special forms
    - evaluate based on boolean value in `cond` or `if` special forms
    
## Q1 
**What would the above statement be translated in the scheme interpreter?**

`(Pair '+' (Pair 1 Pair('*' Pair (2 Pair(3 nil)))), nil)`

Answer: 
`(+ 1 (* 2 3))`

### Special form `and` note
- If any argument evaluates to a false value (in Scheme, only #f is false), it immediately returns #f without evaluating the rest.
- If all arguments are true, it returns the value of the last argument.
```scm
(and (< 1 0) (/ 1 0)) ; false and doesn't have the expection error of 1 / 0 
```

## Q2
**Which of the following are evaluated when scheme_eval is called on in an environment in which x is bound to -2? (Assume <, -, and = have their default values.)**


```scm
(define x -2)

(if (< x 0) (- x) (if (= x -2) 100 y))

#| if x is -2; what symbols evaluate 

if ; not evaluated 
< ; evaluated
= ; not evaluated
x ; evaluated
y ; not
0 ; evaluated
-2 ; not evaluated because it is primitive => already evaluated
100 ; not evaluated
- ; evaluated 
( ; not
) ; not 

|#

```

- **The question distinguishes between symbols being looked up and literals being self-evaluated.**
    - The number -2 is indeed evaluated (it produces the value -2), but it is not looked up as a symbol.


## Q3

__Define `print_evals`, which takes a Scheme expression `expr` that contains only `numbers, +, *,` and `parentheses`. It prints all of the expressions that are evaluated during the evaluation of `expr`. They are printed in the order that they are passed to scheme_eval.__
- Calling print on a Pair instance will print the Scheme expression it represents.
- This problem can be solved with `expr.map(print_evals)`

```scm
>>> nested_expr = Pair('+', Pair(Pair('*', Pair(3, Pair(4, nil))), Pair(5, nil)))
>>> print_evals(nested_expr)
(+ (* 3 4) 5)
+
(* 3 4)
*
3
4
5

```

```python
class Pair:
    "A Scheme list is a Pair in which 
rest is a Pair or nil."
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

def print_evals(expr):
    if not isinstance(expr, Pair):
        "*** YOUR CODE HERE ***" # base 
        print(expr)
    else:
        "*** YOUR CODE HERE ***"
        print(expr)
        while expr is not nil: 
            print_evals(expr.first)
            expr = expr.rest
```