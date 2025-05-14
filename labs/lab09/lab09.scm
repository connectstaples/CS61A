(define (over-or-under num1 num2) 
  (cond 
  (if (< num1 num2) (display "-1"))
  (if (= num1 num2) (display "0")) 
  (if (> num1 num2) (display "1"))
  )
)


(define (make-adder num) 
  (lambda (inc) (+ num inc))
)

(define (composed f g) 
  (lambda (x) 
    (
      f (g x)
    )
  )
)


(define (repeat f n) 
  (if (> n 0) (
                composed f (repeat f (- n 1))
              )
(lambda (x) x)
  )
)

(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))


(define (gcd a b) 
  (cond
    (
      (zero? (modulo a b))
    b)
    
    (else (gcd b (modulo a b))
    )
  )
)
