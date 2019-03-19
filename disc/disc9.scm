; Macros & Streams

;; 1 Macros
; 1.1 Write a macro that takes an expression and a number n and repeats the expression n times.
(define (replicate x n)
    ; (print x)
    (if (= n 0) nil
        (cons x (replicate x (- n 1)))))

(define-macro (repeat-n expr n)
    (cons 'begin (replicate expr n)))

(repeat-n (print '(resistance is futile)) 4)
; replicate接收到的是(print '(resistance is futile))这个list本身, 不是这个expr被evaluated以后的值. 下面是我们想要通过这个macro转化出来的代码
; (begin
;     (print '(resistance is futile))
;     (print '(resistance is futile))
;     (print '(resistance is futile))
;     (print '(resistance is futile)))


; 1.2 Write a macro that takes in two expressions and or's them together(applying short-circuting rules). However, do this without using the or special form. You may also assume the name v1 doesn't appear anywhere outside of our macro.
(define-macro (or-macro expr1 expr2)
    `(let ((v1 ,expr1))
          (if v1 v1 ,expr2)))

; 1.3 Write a macro that takes in a call expression and strips out every other argument. The first argument is kept, the second is removed, and so on. You may find it helpful to write a helper function.
; prune every other element in lst
(define (prune-helper lst)
    (if (or (null? lst) (null? (cdr lst)))
        lst
        (cons (car lst) (prune-helper (cdr (cdr lst))))))

(define-macro (prune-expr expr)
    (cons (car expr) (prune-helper (cdr expr))))

;; 2 Streams
; 2.2 Write a function range-stream which takes a start and end, and returns a stream that represents the integers between start and end - 1 (inclusive) .
(define (range-stream start end)
    (if (= start end)
        nil
        (cons-stream start (range-stream (+ start 1) end))))

; 2.3 Write a function slice which takes in a stream s, a start, and an end. It should return a Scheme list that contains the elements of s between index start and end, not including end. If the stream ends before end, you can return nil.
(define (slice s start end)
    (cond ((or (null? s) (= end 0)) nil)
          ((> start 0)
            (slice (cdr-stream s) (- start 1) (- end 1))
          (else
            (cons (car s)
                (slice (cdr-stream s) (- start 1) (- end 1)))))))

(define (naturals num)
    (cons-stream num (naturals (+ num 1))))
; (define nat (naturals 1))
; (slice nat 4 12) ---> (4 5 6 7 8 9 10 11)

; 2.4 Combine infinite streams
(define (combine-with f xs ys)
    (if (or (null? xs) (null? ys))
        nil
        (cons-stream
            (f (car xs) (car ys))
            (combine-with f (cdr-stream xs) (cdr-stream ys)))))

(define evens (combine-with + (naturals 0) (naturals 0)))
; (slice evens 0 10) ---> (0 2 4 6 8 10 12 14 16 18)

; i.
(define factorials
    (cons-stream 1 (combine-with * (naturals 1) factorials)))

; (slice factorials 0 10) ---> (1 1 2 6 24 120 720 5040 40320 362880)

; ii.
(define fibs
    (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))))

; (slice fibs 0 10) ---> (0 1 1 2 3 5 8 13 21 34)

; iii. Write exp, which returns a stream where the nth term represents the degree-n polynomial expansion for e^x.

(define (exp x)
    (let ((terms (combine-with (lambda (a b) (/ (expt x a) b))
                               (cdr-stream (naturals 0))
                               (cdr-stream factorials))))
        (cons-stream 1 (combine-with + terms (exp x)))))

; (slice (exp 2) 0 5) ---> (1 3 5 6.333333333 7 7.266666667)
