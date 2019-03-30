; Q1
(define (compose-all funcs)
    (if (null? funcs)
        (lambda (x) x)
    (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
)

; Q2
(define (tail-replicate x n)
    (define (tail-replicate-helper x replicate-so-far n)
        (if (= n 0)
            replicate-so-far
            (tail-replicate-helper x (cons x replicate-so-far) (- n 1))))
    (tail-replicate-helper x nil n)
)

