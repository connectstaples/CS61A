#### CS61A Sp25 Apollo Loh
# Macros
#### Sean Villegas

## Macros are about rewriting code before evaluation
- `define-macro` is a **transformation rule**. You are not evaluating expressions yet, your generating new code that will eventually run
- e.g.
    - 
    ```scm
    > (define-macro (foo x) `(+ ,x, x))
    > (foo 3) ; (+ 3 3) is evaluated at runtime and is called macro-expansion time
    6
    ```
- Macro expansion runs happens before runtime 
- If you `eval` inside a macro, it happens at **expansion time, not runtime**.
    - **why would you do that**? _see question 2_ 

### Two phases of the `define-macro`
1. Macro expansion time = when your macro's template runs and returns a new expression (using quasiquote and unquote).
2. Runtime = when the Scheme interpreter evaluates the result of macro expansion.



## How do we evaluate macros? 
- we want to _construct_ an expression to evaluate 
    - that is why we used a `'` in front of begin 
- in the backend, `define-macro` will wait for an expression, and it will evaluate the expression for us

**`define-macro` steps:** 
1. Binding the formal parameters of the macro to the unevaluated operand expressions of the macro call.
2. Evaluating the body of the macro, which returns an expression.
3. Evaluating the expression returned by the macro in the environment of the original macro call.


**Without `define-macro`**
1. define the same expression with ' 
2. call the new procedure with a quoted argument
3. Call eval on the returned expression 

## Q1 Mystery Macro 
```scm
(define-macro (mystery-macro expr old new)
    (mystery-helper expr old new))

(define (mystery-helper e o n)
  (if (pair? e)
      (cons (mystery-helper (car e) o n) (mystery-helper (cdr e) o n))
      (if (eq? e o) n e)))
; eq? is a built in operator for equal in scheme 


; doctests

#| 
scm> (define five 5)
five
scm> (mystery-macro (* x x) x five)
25
scm> (mystery-macro (* x x) x (+ five 1))
36
scm> (mystery-macro '(* x x) x y)
(* y y)
scm> (mystery-macro (> (x) (> (y) (+ x y))) > lambda)
(lambda (x) (lambda (y) (+ x y)))
scm> (mystery-macro (begin e e e) e (print five))
5
5
5

|#
```


## Q2 Multiple Assignment
- Recall that `macros` want to build code to be evaluated at runtime
- Recall that a `macro` life cycle has a expansion time and runtime 
- To swap values, we want to make sure that the evaluation at expansion time will actually map to the values of both original x and y, instead of creating new bindings that drop the old ones. 
- It’s up to the macro author to decide which things to evaluate early and which to leave for later.

```python
>>> x, y = 1 + 1, 3  # now x is bound to 2 and y is bound to 3
>>> x, y = y, x      # swap the values of x and y
>>> x
3
>>> y
2
```

```scm
scm> (assign x y (+ 1 1) 3)  ; now x is bound to 2 and y is bound to 3
scm> (assign x y y x)        ; swap the values of x and y
scm> x
3
scm> y
2

```
Implement the assign Scheme macro, which takes in two symbols sym1 and sym2 as well as two expressions expr1 and expr2. It should bind sym1 to the value of expr1 and sym2 to the value of expr2 in the environment from which the macro was called.

```scm
(define-macro (assign sym1 sym2 expr1 expr2)
  `(begin
     (define ,sym1 ,expr1)
     (define ___ ___)))

; what happens under hood example
(assign x y (+ 1 1) 3)

(eval 
    (begin 
        (define x (+ 1 1))
        (define y (eval 3))
    ))

(eval 
    (begin 
        (define x 2)
        (define y '3)
    ))

```
Make sure that expr2 is evaluated before sym1 is changed. Assume that expr1 and expr2 do not have side effects (and so do not contain define or assign expressions).

## Q3 Switch 

Steps:
- Bind val to the evaluated expr using a let.
- Build a cond clause where:
    - Each condition is (equal? val <case-key>) → done with (car case)
    - Each body is the expression inside that case → done with (cdr case)
- The user gives us a list of pairs, so we can safely assume (car case) is the number, (cdr case) is the expression.


Define the macro switch, which takes in an expression expr and a list of pairs called cases where the first element of the pair is some number and the second element is a single expression. switch will evaluate the expression contained in of cases that corresponds to the number that expr evaluates to.

You may assume that the value expr evaluates to is always the first element of one of the pairs in cases. You can also assume that the first value of each pair in cases is a number and the second expression does not contain the symbol val.

- use `eq?`

```scm
(define-macro (switch expr cases)
    `(let ((val ,expr))
      ,(cons
        'YOUR-CODE-HERE
        (map (lambda (case) (cons
               'YOUR-CODE-HERE
               (cdr case)))
             cases))))

; doctests
scm> (switch (+ 1 1) ((1 (print 'a))
                      (2 (print 'b))
                      (3 (print 'c))))


(let ((val (+ 1 1)))
     (cond ((equal? val 1) (print 'a))
           ((equal? val 2) (print 'b))
           ((equal? val 3) (print 'c))))

(define-macro (switch expr cases)
    `(let ((val ,expr))
      ,(cons
        'cond
        (map (lambda (case) (cons `(equal? val ,(car case)) (cdr case)))
             cases))))
```

In macro expansion:
- we set up a full line of pair lists with quasaquoting
- we let the val be binded to expr temporarily, with a `,` to put the evaluated expr in the string format during expansion
- we then put a `,` to set up a cons cell (a pair list) of a cond, this cond has a  `'`  to put it in list format (pair)
- the cond will have a map procedure within it. it has the procedure lambda named case (can be named anything), that creates its own pair list with cons
- Inside the cons we will check if val and the expr are equal for all the cases (called case), we start with (car case) i.e. the first part of the list of case, and the cdr of case which is the rest of the list
- map will apply the `lambda (case) (...)` to `cases` 