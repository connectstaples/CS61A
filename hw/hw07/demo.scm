(lambda (x) (* x x)) ; square lambda 
; ((lambda (x) (* x x)) 8) ; calling lambda 

(define (square x) (* x x)) 

(define (pow base exp)
    (cond 
        ((= exp 0) 1)
        ((= exp 1) base)
        (even? exp) (pow (square base) (/ exp 2))
        (odd? exp) (* base (pow (square base) (/ (- exp 1) 2)))
    )
)

(define (pow base exp)
  (cond 
    ((= exp 0) 1)
    ((= exp 1) base)
    ((even? exp) (pow (square base) (/ exp 2)))
    ((odd? exp) (* base (pow (square base) (/ (- exp 1) 2))))
  )
)


(display (pow 2 5))

(define (repeatedly-cube n x)
        (if (zero? n) x
            (let 
                (y (repeatedly-cube (- n 1) x))
            )
                (* y y y)
        )
)

(repeatedly-cube 3 3)

(define (cddr s)
' drops the first two elements, gives you the rest of the list
    (cddr (cddr s)) ; return the rest of the rest of cons cell 
) 

(define (caddr s)
' returns the second element of a list
    (car (cdr s))
)

(define (caddr s)
'returns the third element of a list
    (car (cddr s)) ; cddr drops first two elements, car pulls the third element
)

(define (nth-element s n)
    'procedure that allows for indexing elements of a cons cell 
  (if (= n 0)
      (car s)
      (nth-element (cdr s) (- n 1))))


#|

Main takeaway: 
    In scheme, evaluating cons is important to skip past lazy promises instead of computing the whole 
    cons cell. 

(define (square x) 
    (lambda (x) (* x x))
)

(define (square x z) (lambda (x z) (* x z)))

(define square (lambda (x) (* x x)))
|# 

