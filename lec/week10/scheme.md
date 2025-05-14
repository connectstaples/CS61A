#### CS61A, Prof Denero Spring 2025
# Scheme
#### Sean Villegas

[Lecture Videos](https://www.youtube.com/watch?v=esIvijecRFw&list=PL6BsET-8jgYWGDX7c-OKSMCh4QCBZ7Bs4&index=1)

[Review](https://github.com/jianzhi-1/cs61a/blob/main/lec28_scheme_ii.md)

[TLDR](https://cs61a.org/articles/scheme-spec/)
- Read code from inner parenthesis

Background: 
- UCB Scheme is a modified version of STk 4.0.1 by Erick Gallesio. 
- Lisp Language, second oldest programming language
- For current versions of STk, please visit [this](http://kaolin.unice.fr/STk/)

## Rules & Functionality 
- You can have multiline spacing as you please, convention is to create indentation so it is readable. Always close the statements with your parenthesis though.
- Just as in python, there can only be one else statement and it must be at the end of the if statement
- `describe` allows for reuse-ability 
- `cond` handles multiple other if else logic
- `if` handles just two alternatives, in addition to else
- `begin` special form combines multiple expressions into one expression
    - e.g. an `if` statement with multiple lines of logic
- `let` binds symbols to values _temporarily_ (e.g. for one expression, can be defined in a function to be reuseable)
    - good for temporary information 
- `procedure` is a fancy way of saying `function`
    - You can override built procedures in your current environment  
- Scheme programs consist of expressions, which are either call expressions or special forms
- The `logo` language (another lisp dialect) provides a built-in turtle graphics for drawing that can be called in scheme once imported
    - Commands:
    ```scheme
    #/
    Draws lines based on commands  
    /#
    forward ; or fd
    left ; or lt
    right ; or rt
    back ; or bk

    ```



- Comments
    ```scheme 
    #|
    This is a multi-line comment.
    |#

    (<some expression>) ; A semicolon is how you comment out
    ```
- Output to terminal 
    ```scheme
    (print "Hello")  ; Prints "Hello" with a newline

    (display "Hello")  ; Prints "Hello" without a newline
    ```
## Primitive Types
- `#t`, `#f` represent Truthy and Falsy values
- All math expressions
- Everything else (numbers, strings, symbols, even `0` and `""` are **true**)

## Special Forms
- `define`

```scheme 
(define x 2) 
; the interpreter would print `x`, x is bound to 2

(+ 2 x) ; add 2 to x 
; output would be 4

(define x (+ 2 2)) 
; define a new variable with sub expression of math
x ; x is 4 
```

- `defines` procedure 
```scheme
(define (<name> <param> ...) <body>)
```
```scheme
(define (add a b) (+ a b))

(add 2 3) 

(define (average x y) (/ (+ x y) 2))

(average 30 60) ; 45 
```

## Conditional 
- There is no `return` syntax 
- Thus, the value of the last expression evaluated is automatically returned
```scheme
(define x 20)
(if (> x 0) x -x)
; this says if x > 0, return x; otherwise return -x in interpreter

; with better formatting
(define x 20)
(if (> x 0) 
        x 
            -x)
```

### `cond` Example
```scheme
(cond (< x 0) 'negative (= x 0) 'zero (> x 0) 'positive else 'unknown)

(define (describe x)
  (cond 
    ((< x 0) 'negative)
    ((= x 0) 'zero)
    ((> x 0) 'positive)))

(define (describe x) (cond ((< x 0) 'negative) ((= x 0) 'zero) ((> x 0) 'positive)))

(describe -5) ; → 'negative


```


## Or, And
- `#f` is the only value that is false.
- Evaluates left to right.
- Stops at the first false value (`short-circuit` behavior).
- If all expressions are true, it returns the last evaluated value. 
    - Scheme considers **all the number values** to be `true`. 

### `Or` 
- Returns the first true value.
- If none are true, returns `#f`.
- In this example, even though (> x 10) is true, it never gets evaluated because x (which is 19) is **already** _truthy_.
- the bound value that is returned can be in front or back, and even middle


```scheme
(define x 19) 

(and (> x 10) (< x 20)) ; #t 
(and (> x 10) (< x 20) x) ; outputs 19 
```

_the bound value that is returned can be in front or back, and even middle_

```scheme
(or (< x -10) x (> x 10))
```

## Booleans
```scheme
(and #t #t #f)  ; Returns #f (stops at first false)
(or #f #t #f)   ; Returns #t (stops at first true)
(not #t)        ; Returns #f
```
## Lambda 
- evaluates anon procedures 
- returns a function 
```scheme 
(lambda (x) (+ x 4))
```

## `Begin`
- The `begin` special form is used to evaluate expressions in a particular order.
    -  The expression `s` are evaluated sequentially from left to right, and the value of the last expression is returned. 
    e.g.
```scheme
; function example with recursion
(define (repeat k fn)
  (if (> k 0)
      (begin (fn) 
        (repeat (- k 1) fn))
      nil))
> (define (say-hello) (display "hello\n"))

> (repeat 3 say-hello)
```
_Nonfunction example_
```scheme
(begin
  (define x 5)
  (define y 10)
  (+ x y))
```
_Conditional example_
```scheme
(begin
  (if (> 3 2) (display "Yep\n") (display "Nope\n"))
  "Done")
```

## `Let Form` 
- The let special form binds symbols to values temporarily; just for one expression

```scheme
(define c (let ((a 3)
 (b (+ 2 2)))
 (sqrt (+ (* a a) (* b b)))))

 ; a and b are will not bound outside frame due ot let
```

## `Pairs`

- Pairs are used to combine two Scheme objects into one compound object. Hence the name: A pair stores a pair of objects

```scheme
(define x (cons 1 2))
x         ; Returns (1 . 2)
(car x)   ; Returns 1
(cdr x)   ; Returns 2

(define s (cons 1 (cons 2 nil)))
; > s will return (1, 2) in linked list fashion 

```

## Lists
- Scheme lists are `linked` lists. `nil` is the empty list. 
    - similar to the class `Link` created in python
- `cons` must take two arguments.
    - first value, and then rest of the list
- Scheme has a built-in `list` procedure that will create a list e.g. `(list 3)` 
- To build a list one element at a time, use `cons`
- To build a list with a fixed length, use `list`

```scheme
(cons 1 (cons (2 null))) ; (1, 2)
```
_accessing a list_
```scheme
(define lst (cons 1 (cons 2 nil)))
(car lst) ; 1
(cdr lst) ; (2)
```
## Recursive Lists
- Recursive lists are also built into the language, using pairs.
- A special value denoted `nil` or `'()` represents the empty list. 
- A recursive list value is rendered by placing its elements within parentheses, separated by spaces:

```scheme
(cons 1
      (cons 2
            (cons 3
                  (cons 4 nil))))

; same as below
(cons 1 (cons 2 (cons 3 (cons 4 nil))))  ; Returns (1 2 3 4)

(list 1 2 3 4)  ; Returns (1 2 3 4)

(define one-through-four (list 1 2 3 4))

(car one-through-four)  ; Returns 1

(cdr one-through-four)  ; Returns (2 3 4)

(car (cdr one-through-four))  ; Returns 2

```

## List Operations
- Whether a list is **empty** can be determined using the primitive `null?` predicate.
- Using it, we can define the standard sequence operations for computing length and selecting elements:

```scheme
 (define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))
(define (getitem items n)
  (if (= n 0)
      (car items)
      (getitem (cdr items) (- n 1))))
(define squares (list 1 4 9 16 25))
(length squares)  ; Returns 5
(getitem squares 3)  ; Returns 16
```

## Symbolic Data
- In Scheme, any expression that is not evaluated is said to be quoted.    
    - Derived from philosophy, (e.g. when referring to dog rather than the word "dog" in language)

- Quotation also allows us to type in compound objects, using the conventional printed representation for lists
- Quotation can also be applied to combinations to form lists.
e.g.
    ```scheme
    '(a b c) ; (a b c)
    (car '(a b c)) ; a 
    (cdr '(a b c)) ; (b c)
    ```

```scheme
(define a 1)
(define b 2)
(list a b)      ; Returns (1 2)
(list 'a 'b)    ; Returns (a b)
(list 'a b)     ; Returns (a 2)
(list 'define 'list)  ; Returns (define list)
(car '(a b c))  ; Returns a
(cdr '(a b c))  ; Returns (b c)
```

```scheme
(list 'a 'b) ; (a, b)
(list 'a b)  ; (a, 2)
(list (quote a) (quote b)) ; (a, b) ; does the same thing as ' 
```

_focus on how Scheme can manipulate symbols as immutable data without altering the original bindings_
- `a` isnt defined and still works 
```scheme
scm> '(a b c)
(a b c)
scm> (car '(a b c))
a
```


## Turtle Graphics

```scheme
(define (repeat k fn)
  (if (> k 0)
      (begin (fn) (repeat (- k 1) fn))
      nil))
(repeat 5
        (lambda ()
          (fd 100)
          (repeat 5
                  (lambda () (fd 20) (rt 144)))
          (rt 144)))  ; Draws a star-like pattern

(define (repeat k fn)
  (if (> k 0)
      (begin (fn) (repeat (- k 1) fn))
      nil))
(define (tri fn)
  (repeat 3 (lambda () (fn) (lt 120))))
(define (sier d k)
  (tri (lambda ()
         (if (= k 1) (fd d) (leg d k)))))
(define (leg d k)
  (sier (/ d 2) (- k 1))
  (penup)
  (fd d)
  (pendown))
(sier 100 4)  ; Draws a Sierpinski triangle with depth 4 and initial size 100   
```

##  Future
- The full Scheme language contains additional features, such as mutation operations, vectors, and maps. 


## Lecture 27 
# Scheme Lists

- `(append s t)` list the elements of s and t; append can be called on more than 2 lists 
- `(map f s)` call a procedure f on each element of a list s and list the results 
- `(filter f s)` call a procedure f on each element of a list s and list the elements for which a true value is the result 
- `(apply f s)` call a procedure f with the elements of a list s as its arguments
- `append` expects **all** of its parameters passed in to be lists as its arguments 
- `(cons 1 2)` is `(1 . 2)` because of no `nil` at end to represent empty list 
- `(cons 1 (cons 2 nill))` will be `(1 2)`
```scheme
; list mutation examples

(define x (cons 10 (cons 11 nil))) ; (10 11)

(list 3 x); (3 (10 11))

(cons 3 s); (3 3 (10 11))

; (append 3 s) ; error because append requires list data type 

(list x x); (3 3 (10 11) (3 3 (10 11)))

(cons x 3); (3 3 (10 11) (3 3 (10 11)) . 3)

(define z (cons 4 nil)); z is (4)

(append x z); (3 3 (10 11) (3 3 (10 11)) . 3 4 )
```