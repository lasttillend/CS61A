; CSM6: Scheme

; 2 Hailstone yet again

(define (hailstone seed n)
  (cond ((= n 0) seed)
        ((even? seed)
         (hailstone (quotient seed 2) (- n 1)))
        ((odd? seed)
         (hailstone (+ (* seed 3) 1) (- n 1))))
)

; 4 Define Well-formed, which determines whether lst is well-formed list or not. Assume lst only contains numbers.

(define (well-formed lst)
    (cond ((null? lst) #t)
          ((list? (cdr lst)) (well-formed (cdr lst)))
          (else #f))
)

; 5 Define is-prefix, which takes in a list p and a list lst and determines if p is a prefix of lst.

(define (is-prefix p lst)
    (cond ((null? p) #t)
          ((> (length p) (length lst)) #f)
          ((= (car p) (car lst)) (is-prefix (cdr p) (cdr lst)))
          (else #f))
)

(define (deep-map fn lst)
  (if (null? lst)
      nil
      (if (list? (car lst))
          (cons (deep-map fn (car lst)) (deep-map fn (cdr lst)))
          (cons (fn (car lst)) (deep-map fn (cdr lst)))
   )
 )


