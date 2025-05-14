#### CS61A Prof Denero 
# Scheme Lists and Calculator
#### Sean Villegas

- `(append s t)` list the elements of s and t; append can be called on more than 2 lists 
- `(map f s)` call a procedure f on each element of a list s and list the results 
- `(filter f s)` call a procedure f on each element of a list s and list the elements for which a true value is the result 
- `(apply f s)` call a procedure f with the elements of a list s as its arguments **ONCE** 
- `append` expects **all** of its parameters passed in to be lists as its arguments 
- `(cons 1 2)` is `(1 . 2)` because of no `nil` at end to represent empty list 
- `(cons 1 (cons 2 nill))` will be `(1 2)`


## `Eval` Func
- The eval function computes the value of an **expression**, which is always a **number**
- It is a generic function that dispatches on the type of the expression (primitive or call)

Semantics: 
- A number evaluates to itself 
- A call expression evaluates to its argument values combined by an operator (e.g. arithmetic)

```python
def calc_eval(expression):
    if isinstance(expression, (int, float)):
        return expression
    elif isinstance(expression, Pair):
        arguments = expression.rest.map(calc_eval)
        return calc_apply(expression.first, arguments)
    else:
        raise TypeError

```
## Read-Eval-Print Loop 
The user interface for many programming languages is an interactive interpreter
1. Print a prompt
2. Read text input from the user
3. Parse the text input into an expression
4. Evaluate the expression
5. If any errors occur, report those errors, otherwise
6. Print the value of the expression and repeat