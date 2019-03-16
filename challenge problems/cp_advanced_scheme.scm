; Challenge Problems: Advanced Scheme

;; 1. Functions and Lambda
; (a) Write filter. filter takes in a list and another predicate function, and returns a list of only the items that satisfy this predicate funciton.
; (filter '(1 2 3 4 5 6 7) (lambda (x) (= (modulo x 3) 0))) ---> (3 6)
(define (filter lst fn)
    (cond ((null? lst) nil)
          ((fn (car lst)) (cons (car lst) (filter (cdr lst) fn)))
          (else (filter (cdr lst) fn)))
)

; (b) Write map, which takes in a list and a funciton, and returns a new list with the same elements but with the function applied to them.
; (map '(1 2 3 4 5 6 7) (lambda (x) (* x x))) ---> (1 4 9 16 25 46 49)
(define (map lst fn)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map (cdr lst) fn)))
)

; (c) Write accumulate. accumulate is the Scheme version of reduce in Python. It takes in a list, a funciton, and a seed. It condenses (or accumulates) the elements of the list using the funciton, where the starting point is the seed.
; (accumulate '(1 2 3 4 5 6 7) (lambda (x y) (+ x y)) 0) ---> 28
; (accumulate '(1 2 3 4 5 6 7) (lambda (x y) (* x y)) 1) ---> 5040 ; 7!
(define (accumulate lst fn seed)
    (if (null? lst)
        seed
        (accumulate (cdr lst) fn (fn (car lst) seed)))
)

; (d) Write the function compose, which takes in two functions f and g and evaluates to a new function that is the composition f(g(.)). Assume f and g are single-argument functions.
; ((compose (lambda (x) (* x x)) (lambda (x) (+ x 2))) 4) ---> 36
(define (compose f g)
    (lambda (x) (f (g x)))
)

; (e) Write the function safe-fn. safe-fn takes in a regular single-argument funciton and a predicate function, and evaluates to a new function that is a safer version by checking the argument using the predicate before evaluating.
; ((safe-fn sqrt (lambda (x) (and (number? x) (> x 0)))) 16) ---> 4
; ((safe-fn sqrt (lambda (x) (and (number? x) (> x 0)))) "not a number") ---> #f
; ((safe-fn sqrt (lambda (x) (and (number? x) (> x 0)))) -1) ---> #f
(define (safe-fn fn pred)
    (lambda (x)
        (if (pred x) (fn x) #f))
)

; (f) Write a function replicate that takes in a list and returns a new list with each element replicated k times.
; (replicate '(1 2 3) 3) ---> (1 1 1 2 2 2 3 3 3)
(define (replicate-k num k)
    (if (= k 0) nil (cons num (replicate-k num (- k 1))))
)

(define (flatten lst)
    (cond ((null? lst) nil)
        ((list? (car lst)) (append (flatten (car lst)) (flatten (cdr lst))))
        (else (cons (car lst) (flatten (cdr lst)))))
)

(define (replicate lst k)
    (flatten (map lst (lambda (num) (replicate-k num k))))
)

; (g) Write a function remove-k that removes the kth element from a given list.
; (remove-k '(0 1 2 3 4 5) 4) ---> (0 1 2 3 5)
(define (remove-k lst k)
    (if (= k 0)
        (cdr lst)
        (cons (car lst) (remove-k (cdr lst) (- k 1))))
)

; (h) Given a run-length encoding, write a function decode that turns an encoded list of elements and their counts into the original list. The encoded list consists of the same elements, but where there is a run of more than 1 of the same element in a row, they are condensed into a pair.
; (define code '((a . 4) (b . 2) c a (b . 3)))
; (decode code) ---> (a a a a b b c a b b b)
(define (decode lst)
    (cond ((null? lst) nil)
          ((pair? (car lst)) (append (replicate-k (car (car lst)) (cdr (car lst))) (decode (cdr lst))))
          (else (cons (car lst) (decode (cdr lst)))))
)

; (i) Write the corresponding encode function that turns a list of elements into a run-length encoded list.
; (encode '(a b b b c d d e a)) ---> (a (b . 3) c (d . 2) e a)
; (equal? (encode (decode code))) ---> #t
(define (encode-helper lst item run)
    (cond ((null? lst) (list (cons item run)))
          ((eq? item (car lst)) (encode-helper (cdr lst) item (+ run 1)))
          (else (cons (cons item run) (encode-helper (cdr lst) (car lst) 1))))
)

(define (encode lst)
    (map (encode-helper (cdr lst) (car lst) 1)
        (lambda (pair) (if (= (cdr pair) 1) (car pair) pair)))
)

;; 2. Tail Calls
; (a) Here is a definition for a modified summing procedure that sums up the elements of a list. Rewrite the function to be tail-recursive.
(define (sum lst fn)
    (cond ((null? lst) 0)
          (else (+ (fn (car lst)) (sum (cdr lst) fn))))
)

(define (sum-tail lst fn)
    (define (sum-tail-helper lst ret)
        (if (null? lst)
            ret
            (sum-tail-helper (cdr lst) (+ ret (fn (car lst))))))
    (sum-tail-helper lst 0)
)

; (b) Write the function power that raises x to the power y so that it is tail-recursive
; (power 2 5) ---> 32
(define (power-helper base exp ret)
    (if (= exp 0)
        ret
        (power-helper base (- exp 1) (* ret base)))
)

(define (power base exp)
    (power-helper base exp 1)
)
; non-tail recursive version
(define (power2 base exp)
    (if (= exp 0)
        1
        (* base (power2 base (- exp 1))))
)

