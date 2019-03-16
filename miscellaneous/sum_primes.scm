;; Sequence operations

;; Map f over s.
(define (map f s)
  (if (null? s)
      nil
      (cons (f (car s))
            (map f
                 (cdr s)))))

;; Filter s by f.
(define (filter f s)
  (if (null? s)
      nil
      (if (f (car s))
          (cons (car s)
                (filter f (cdr s)))
          (filter f (cdr s)))))

;; Reduce s using f and start value.
(define (reduce f s start)
  (if (null? s)
      start
      (reduce f
              (cdr s)
              (f start (car s)))))

;; Primes

;; List integers from a to b.
(define (range a b)
  (if (>= a b) nil (cons a (range (+ a 1) b))))

;; Sum elements of s
(define (sum s)
  (reduce + s 0))

;; Is x prime?
(define (prime? x)
  (if (<= x 1)
      false
      (null?
       (filter (lambda (y) (= 0 (remainder x y)))
               (range 2 x)))))

;; Sum primes from a to b
(define (sum-primes a b)
  (sum (filter prime? (range a b))))
