#### CS61A Prof Denero 
# Interpreters 
#### Sean Villegas



# Pairs in Project 4

- **IMPORTANT NOTE**: Since all non-atomic Scheme expressions (i.e., call expressions, special forms, definitions) are Scheme lists (and therefore linked lists), we use the Pair class to represent them. 
- The Pair class is similar to the Link class we've been working with. For example, the expression (+ 1 2) will be represented in our interpreter as Pair('+', Pair(1, Pair(2, nil))). More complicated expressions can be represented with nested Pairs. For example, the expression(+ 1 (* 2 3)) will be represented as Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil))). 
- The Pair class is defined in pair.py. Notice the similarities with the Link class.

- Pair is like class Link in Cs61a

Tokenization/Parsing: Converts text into Python representation of Scheme expressions:

- Numbers are represented as numbers
- Symbols are represented as strings
- Lists are represented as instances of the Pair class

Evaluation: Converts Scheme expressions to values while executing side effects:
- scheme_eval(expr, env) returns the value of an expression in an environment
- scheme_apply(procedure, args) applies a procedure to its arguments
0 The Python function scheme_apply returns the return value of the procedure it applies

```scheme
(if <predicate> <consequent> <alternative>)
(define <name> <expression>)
(lambda (<formal-parameters>) <body>)
(<operator> <operand 0> ... <operand k>)
```

# Frames
- A frame represents an environment by having a parent frame
- Frames are Python instances with methods lookup and define
- In Project 4, Frames do not hold return values

# Special Forms
- built in procedures can take in built in procedures such as: 
    - `odd?`
    - `even?`
    - `apply`
- Conventional note: a procedure that returns `T/F` generally has a `?` in the procedure name, it has no effect on the function 
- `apply` applies once on **ALL** elements
- `map` applied for **EACH ELEMENT** and _returns list_
- `append` will combine list the elements in terminal 

## Valid scheme statements: 
```scheme
> (define s '(3 4 5))
> (define t (list 6 7))
> (define u '(8 9 10))
> (map <procedure> (filter odd? (append s t u))) ; valid statement
> (filter odd? (map <procedure> (append s t u)))
```

## Notes on `list` and `cons`
```scheme
> (cons 3 nil) ; != to (list 3 nil)
(3)
> (list 3 nil) ; != (cons 3 nil)
(3 ())
```

### Visual Representation
`cons`
```scheme 
> (cons (3 nil))
(3)
```
Will look like: 
```text
-> [3][()]
```
`list`
```scheme 
> (list 3 nil) 
(3 ())
```
Will look like: 
```text
-> [3][] -> [()][()]
```