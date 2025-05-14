; function example with recursion

(define (repeat k fn)
  (if (> k 0)
      (begin (fn) 
        (repeat (- k 1) fn))
      nil))

(define (say-hello) (display "hello\n"))

(define (repeat k fn) (if > k 0) (begin (fn) (repeat (- k 1) fn)) nill)

(define (repeat k fn) (if (> k 0) (begin (fn) (repeat (- k 1) fn)))) ; will return hello but without the () at the end

(repeat 3 say-hello) ; wwsp?
#| 
hello
hello
hello
()
|#

; nonfunction ex
(begin
  (define x 5) ; x is binded to 5
  (define y 10) ; y is binded to 10 
  (+ x y)) ; 10 

; conditional logic
(begin 
(if (> 3 2) (display "Yep\n") (display "Nope\n"))
  "Done")

#|
if 3 is greater than 2, elif display Yep new line
else display Nope new line
|# 


(let ((x 5)) ; 5 plus 4 due to frames. x is 5 outside 
    (let ((x 2)
         (y x))
       (+ y (* x 2))))


(define (enumerate s) (
  ; BEGIN PROBLEM 15
  let ((i 0))
  (define (enumerate-helper s index)
      (if (null? s) '()
      (cons (cons index (cons(car s) '())) (enumerate-helper (cdr s) (+ index 1)))))
    (enumerate-helper s i))
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists S1 and S2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? s1 s2)
  ; BEGIN PROBLEM 16
  (cond ((null? s1) s2)
    ((null? s2) s1)
    ((ordered? (car s1) (car s2)) (cons (car s1) (merge ordered? (cdr s1) s2)))
    (else (cons (car s2) (merge ordered? s1 (cdr s2))))
    )
  )
  ; END PROBLEM 16
