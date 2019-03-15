; Tail Recursion and Interpreters

; 5 Filter
(define (reverse lst)
    (define (reverse-sofar lst lst-sofar)
        (if (null? lst)
            lst-sofar
            (reverse-sofar (cdr lst) (cons (car lst) lst-sofar))))
    (reverse-sofar lst nil)
)

(define (append a b)
    (define (rev-append-tail a b)
        (if (null? a)
            b
            (rev-append-tail (cdr a) (cons (car a) b))))
    (rev-append-tail (reverse a) b)
)

(define (filter f lst)
    (define (rev-filter-tail lst)
        (if (null? lst)
            nil
            (if (f (car lst))
                (append (rev-filter-tail (cdr lst)) (list (car lst)))
                (rev-filter-tail (cdr lst)))))

    (rev-filter-tail (reverse lst))
)
