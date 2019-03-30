; Q4
(define (rle s)
    (define (rle-helper s item run)
        (cond ((null? s) (cons-stream (list item run) nil))
              ((= (car s) item) (rle-helper (cdr-stream s) item (+ run 1)))
              (else (cons-stream (list item run) (rle-helper (cdr-stream s) (car s) 1)))))
    (if (null? s)
        nil
        (rle-helper (cdr-stream s) (car s) 1))
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
    (define (tail-insert-helper n s insert-lst-so-far)
        (if (or (null? s) (< n (car s)))
            (append insert-lst-so-far
                    (cons n s))
            (tail-insert-helper
                        n
                        (cdr s)
                        (append insert-lst-so-far
                                (list (car s))))))
    (tail-insert-helper n s nil)
)

; Q6
(define (deep-map fn s)
    (cond ((null? s) nil)
          ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
          (else (cons (fn (car s)) (deep-map fn (cdr s)))))
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
    (if (null? s)
        nil
        (cons (car s) (filter (lambda (x) (not (eq? x (car s)))) (unique (cdr s)))))
)

(define (count name s)
    (cond ((null? s) 0)
          ((eq? name (car s)) (+ 1 (count name (cdr s))))
          (else (count name (cdr s))))
)

(define (tally names)
    (map (lambda (name) (cons name (count name names))) (unique names))
)
