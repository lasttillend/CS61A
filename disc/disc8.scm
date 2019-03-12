;; 3.4 Insert a number into a sorted list using tail recursion
; a
(define (reverse lst)
    (define (reverse-sofar lst lst-sofar)
        (if (null? lst)
            lst-sofar
            (reverse-sofar (cdr lst) (cons (car lst) lst-sofar))))
    (reverse-sofar lst nil)
)

; b
(define (append a b)
    (define (rev-append-tail a b)
        (if (null? a)
            b
            (rev-append-tail (cdr a) (cons (car a) b))))
    (rev-append-tail (reverse a) b)
)

; c
(define (insert n lst)
    (define (rev-insert lst rev-lst)
        (cond ((null? lst) (cons n rev-lst))
              ((> (car lst) n) (rev-insert (cdr lst) (cons (car lst) rev-lst)))
              (else (append (reverse lst) (cons n rev-lst)))))
    (rev-insert (reverse lst) nil)
)
