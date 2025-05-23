 (define (ascending? s)
    (cond 
        ((or (null? s) (null? (cdr s))) #t)
        ((>= (car(cdr s)) (car s)) (ascending? (cdr s)))
        (else #f)
    )
)

(define (my-filter pred s)
  (if (null? s)
      '()
      (if (pred (car s))
          (cons (car s) (my-filter pred (cdr s)))
          (my-filter pred (cdr s)))))

(define (interleave lst1 lst2)
  (cond ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (cons (car lst1)
                    (interleave lst2 (cdr lst1))))))

; helper procedure for member
(define (member? x lst)
  (cond
    ((null? lst) #f)
    ((= x (car lst)) #t)
    (else (member? x (cdr lst)))))

(define (no-repeats s)
  (if (null? s)
      '()
      (let ((rest (no-repeats (cdr s))))
        (if (member? (car s) rest)
            rest
            (cons (car s) rest)))))

