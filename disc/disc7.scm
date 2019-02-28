; Disc07 Scheme

; 5.1 concat
(define (concat a b)
    (if (null? a)
        b
        (cons (car a) (concat (cdr a) b))
    )
)

; 5.2 replicate
(define (replicate x n)
    (if (= n 0)
        nil
        (cons x (replicate x (- n 1)))
    )
)

; 5.3 uncompress
(define (uncompress s)
    (if (null? s)
        nil
        (concat (replicate (car (car s)) (car (cdr (car s))))
                (uncompress (cdr s)))
    )
)

; 5.4 map
(define (map fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map fn (cdr lst)))
    )
)

; 5.5 deep-map
(define (deep-map fn lst)
    (if (null? lst)
        nil
        (if (list? (car lst))
            (cons (deep-map fn (car lst)) (deep-map fn (cdr lst)))
            (cons (fn (car lst)) (deep-map fn (cdr lst)))
        )
    )
)

; Extra questions

; 6.1 abstract tree data type
(define (make-tree label branches)
    (cons label branches)
)

(define (label tree)
    (car tree)
)

(define (branches tree)
    (cdr tree)
)

; Examples of trees
; Remember branches are a list of trees!
(define t1 (make-tree 3 (list (make-tree 1 nil) (make-tree 2 nil))))
(define t2 (make-tree 5 nil))
(define t3 (make-tree 6 (list (make-tree 7 nil) (make-tree 8 nil))))
(define t (make-tree 4 (list t1 t2 t3)))

; 6.2 tree-sum
(define (sum lst)
    (if (null? lst)
        0
        (+ (car lst) (sum (cdr lst)))
    )
)

(define (tree-sum tree)
    (+ (label tree) (sum (map tree-sum (branches tree))))
)

; 6.3 path product tree
(define (path-product-tree t)
    (define (path-product t product)
        (let ((prod (* product (label t))))
            (make-tree prod
                (map (lambda (t) (path-product t prod))
                    (branches t))))
    )
    (path-product t 1)
)


