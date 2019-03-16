; Challenge Problems: Basic Scheme

;; 2. Functions on Lists
; (a) Write a function last that takes in a list and returns the last element in the lists.
; (last '(1 2 3 4 (5 6) 7)) ---> 7
; (last '(1 2 3 (4 5))) ---> (4 5)
(define (last lst)
    (cond ((null? lst) nil)
          ((null? (cdr lst)) (car lst))
          (else (last (cdr lst))))
)

; (b) Write a function double that takes in a list and returns a list with every element duplicated. Assume that every element in the list is a single token, and not another list.
; (double '(1 2 3 4)) ---> (1 1 2 2 3 3 4 4)
(define (double lst)
    (if (null? lst)
        nil
        (append (list (car lst) (car lst)) (double (cdr lst))))
)

; (c) You may be familiar with the function that reverses a shallow list. That is, if the list has elements that are also lists, those inner lists are not reversed themselves. Write a function deep-reverse that reverses all elements of the list, including sublists.
; (deep-rev '(1 2 (3 4 5) ((6)) 7 (8 9) 10)) ---> (10 (9 8) 7 ((6)) (5 4 3) 2 1)
(define (deep-rev lst)
    (cond ((null? lst) nil)
          ((list? (car lst)) (append (deep-rev (cdr lst)) (list (deep-rev (car lst)))))
          (else (append (deep-rev (cdr lst)) (list (car lst)))))
)

; (d) Write a function flatten that flattens a list, bringing all elements in sublists to the top level.
; (flatten '(a b (c d) (((e)) f) (g (h (i) j k) l))) ---> (a b c d e f g h i j k l)
(define (flatten lst)
    (cond ((null? lst) nil)
        ((list? (car lst)) (append (flatten (car lst)) (flatten (cdr lst))))
        (else (cons (car lst) (flatten (cdr lst)))))
)

;; 3. Iteration to Recursion in Scheme
; (a) Write a function prime that tests if a number is prime. You may find the function mod useful, which is the equivalent to the % operator to find the remainder in Python.

(define (filter f s)
  (if (null? s)
      nil
      (if (f (car s))
          (cons (car s)
                (filter f (cdr s)))
          (filter f (cdr s)))))

(define (range a b)
    (if (>= a b) nil (cons a (range (+ a 1) b)))
)

(define (prime x)
    (if (<= x 1)
        #f
        (null? (filter (lambda (n) (= (remainder x n) 0)) (range 2 x))))
)

; Method 2
; (define (prime-helper num factor)
;     (cond ((= factor 1) #t)
;     ((= (remainder num factor) 0) #f)
;     (else (prime-helper num (- factor 1)))))

; (define (prime? num)
;     (prime-helper num (- num 1)))

; (b) Write a function fibo that returns the nth Fibonacci number in theta(n) time (so no tree recursion)
(define (fibo-helper n prev curr)
    (if (= n 0)
        prev
        (fibo-helper (- n 1) curr (+ prev curr)))
)

(define (fibo n)
    (fibo-helper n 0 1)
)

