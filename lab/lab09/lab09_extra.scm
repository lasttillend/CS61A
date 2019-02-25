;; Extra Scheme Questions ;;


; Q5
(define lst
  (list (list 1) 2 (cons 3 4) 5)
)

; Q6
(define (composed f g)
  'YOUR-CODE-HERE
  (define (composal x)
    (f (g x)))
  composal
)

; Q7
(define (remove item lst)
  'YOUR-CODE-HERE
  (if (null? lst)
    nil
    (if (= (car lst) item)
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst)))))
)
; Q7 Method 2: using filter procedure
(define (remove2 item lst)
  (filter (lambda (x) (not (eq? x item))) lst)
)

;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  'YOUR-CODE-HERE
  (cond
    ((= a 0) b)
    ((= b 0) a)
    ((< a b) (gcd b a))
    ((= (modulo a b) 0) b)
    (else (gcd b (modulo a b))))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  'YOUR-CODE-HERE
  (if (null? s)
    nil
    (cons (car s)
      (filter (lambda (x) (not (= (car s) x))) (no-repeats (cdr s)))))
)

; Q10
(define (substitute s old new)
  'YOUR-CODE-HERE
  (if (null? s)
    nil
    (if (pair? (car s))
      (cons (substitute (car s) old new)
        (substitute (cdr s) old new))
      (if (eq? (car s) old)
        (cons new (substitute (cdr s) old new))
        (cons (car s) (substitute (cdr s) old new)))))
)

; Q11
(define (sub-all s olds news)
  'YOUR-CODE-HERE
  (if (null? olds)
    s
    (substitute (sub-all s (cdr olds) (cdr news)) (car olds) (car news)))
)
