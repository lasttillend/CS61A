; Scheme and Tail Recursion

; 2. deeval
(define (deeval num k)
    (cond
        ((= num 0) 1)
        ((= k 0) 0) ; ((or (= k 0) (< num 0)) 0)
        (else
            (+
                (if (= (modulo num k) 0)
                    (deeval (/ num k) (- k 1))
                    0
                )
                (deeval (- num k) (- k 1))
            )
        )
    )
)

; 3. num-calls
(define (pair-add p1 p2)
    (if (null? p1)
        nil
    (cons (+ (car p1) (car p2)) (pair-add (cdr p1) (cdr p2)))))

(define (len lst)
    (if (null? lst)
        0
        (+ 1 (cdr lst))))

; 4. isset
(define (isset lst)
    (define (helper )
        (if (null? lst)
            (helper )
            )
        )
    (helper )
    )

; 5. deep-reverse
(define (deep-reverse lst)
    (cond ((null? lst) nil)
          ((list? (car lst)) (append (deep-reverse (cdr lst))
                                     (list (deep-reverse (car lst)))))
          (else (append (deep-reverse (cdr lst))
                        (list (car lst))))))

; (deep-reverse '(foo bar baz)) ---> (baz bar foo)
; (deep-reverse '(1 (2 3) (4 (5 6) 7))) ---> ((7 (6 5) 4) (3 2) 1)
