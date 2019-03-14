(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (accumulate combiner (combiner start (term n)) (- n 1) term))
)
; the above version has already been tail recursive
(define (accumulate-tail combiner start n term)
  (if (= n 0)
      start
      (accumulate-tail combiner (combiner start (term n)) (- n 1) term))
)

(define-macro (list-of expr for var in seq if filter-fn)
    ; (map (lambda (var) expr) (filter (lambda (var) filter-fn) seq))
    ; (list 'map (list 'lambda (list var) expr) (list 'filter (list 'lambda (list var) filter-fn) seq))
    `(map (lambda (,var) ,expr) (filter (lambda (,var) ,filter-fn) ,seq))
)

; if <conditional> optional version
(define-macro (list-of expr for var in lst . args)
    (let ((filtered (if (= (length args ) 2)
                        `(filter (lambda (,var) ,(car (cdr args))),lst)
                        lst)))
        `(map (lambda (,var) ,expr) ,filtered))
)

; Note: In Scheme you can use the dot notation for declaring a procedure that receives a variable number of arguments.
