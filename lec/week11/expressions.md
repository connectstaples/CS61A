#### CS61A Sp25 Prof Denero
# Expressions and Macros
#### Sean Villegas

_topic students struggle with on final_ 

## Notes: 
- Quasiquotation: 
    ```scm
    > `(+, (* 2 3) 1) ; the whole expression isnt evaluated besides after the comma (the sub expression)
    (+ 6 1)
    ```
- `,` tells scheme to evaluate it in **quasiquation** 
    - once something is quosiquoted, you dont need to add more quasiquotes inside the list 
- procedures that return expressions that are scheme lists

### What would we quasiquote to get the evaluation 
`(+ (* a a) (* b b))`

```scm
_(define (square-expr term)_ (_ * _ term _ term))
    _(_ + _ ( _square-expr _a)_ (_square-expr _b))

; 1st attempt
`(define ,(square-expr term) `(* term term))
    `(+ ,(square-expr `a) ,(square-expr `b))

; solution
(define (square-expr term) `(*, term, term) `(+ ,(square-expr `a)) ,(square-expr `b))


```

## Quick Recap of Streams 
_note that dots indicate when the second element of a pair isnt another pair in the scheme.cs61a.org interpreter (removed in class material bc it was confusing for students)_ 

Generators review: 
- allow you to read infinite sequences
- data line by line to save memory and space
- lazy promises denotes lazy evaluation 

Scheme Lazy Promises
- constructed like normal scheme lists, but with cons stream 
- tells scheme not to evaluate `cdr` until it has to; either by user interacting with it or forced
- `cdr` can be a scheme list or stram
- `cdr` **always** gives a promise to evaluate with `cdr stream`

**Promises** arent evaluated until you call `cdr stream`
- forced implies promise is evaluated   
    - `cons-stream` is a promise not forced
- not forced implies promise hasnt evaluated
    - `cdr-stream` is a promise forced



## Programs As Data Note
- `eval` will evaluate the quoted procedure in scheme 
- python has a built in eval that takes a string and tells you its value

## Macros
- **definition:** _operation performed on source code of program **BEFORE** evaluation._
- **Big idea:** you can change the way the language works meaning we have control on how things are evaluated inside a macro 

- macros are easier to define in lisp, but exit in other languages 
- In Lisp and Scheme, code is represented as data structures called pairs (cons cells), which form linked lists
- Macros let you form new special forms implying that we can change the way a program works
- In lisp, code is just data (pairs which are linked lists)
- print calls on variables will print the value passed in, but once you try to access it again it will not be in memory due to evaluated already (in scm interpreter)
    - e.g.
    ```scm
    > (define-macro (twice expr) (list 'begin expr expr))
    > (twice (print 2))
    2
    2
    ; this would not work
    scm> ((print 2) (print 2))
    2
    Traceback (most recent call last):
    0	((print 2) (print 2))
    Error: nonetype is not callable: undefined
    scm> 
    ```
    - why doesn't `((print 2) (print 2))` not work? 
        - If you just write something like ((print 2) (print 2)), the interpreter tries to treat (print 2) as a function and apply it to (print 2), which is not the intended behavior and can cause errors or unexpected results.


### Evaluation of Macros

**TLDR**

`define` procedures evaluation cycle: 
1. evaluate operator 
2. evaluate operands
3. apply operator to operands

`define-macro` procedures evaluation cycle:
1. evaluate operator 
2. apply operator to operands
3. evaluate result
    - operands arent evaluated 
    - return value is treated as code, not the final result
        - then it gets evaluated one more time



1. evaluate operator sub expression then evaluate sub expression later, essentially setting it up 
2. call `define-macro` procedure on operand expression without evaluating the subexpressions first 
3. evaluate expression returned from macro procedure 
    ```scm
    ; example without define-macro 
    > (define (twice expr) (list 'begin expr expr))
    > (twice (print 2))
    2
    (begin None None)

    > (twice '(print 2)) ; doesnt evaluate expression but gives desired results
    (begin (print 2) (print 2))
    > (eval ( (begin (print 2) (print 2))) )
    2
    2
    ```
    - the main idea from the above code is that all that code writing is handled by `define-macro`; passing in a quote or list element that isnt **evaluated** in a define procedure, that then is evaluated later when calling the procedure

### `for` Macro 

```scm
(define-macro (for sym vals expr))
    `(list `map(list `lambda(list sym) expr) vals) ; this is wrong btw 

> (map (lambda (x) (* x x)) '(2 3 4 5)) ; useable but can be cleaner

(define-macro (for sym vals expr)
  `(map (lambda (,sym) ,expr) ,vals))

(for x '(2 3 4 5) (* x x)) ; cleaner then lambda call
```


