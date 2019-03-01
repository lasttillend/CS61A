; Turtle graphics

; pentagram
(define (repeat k fn)
    (if (> k 0)
        (begin (fn) (repeat (- k 1) fn))
        nil)
)

; (repeat 5
;     (lambda () (fd 100)
;                (repeat 5
;                     (lambda () (fd 20) (rt 144)))
;                (rt 144))
; )

; Sierpinski's triangle
(define (tri fn)
    (repeat 3 (lambda () (fn) (lt 120)))
)

; sier画Sierpinski三角形，等价于画三个角
(define (sier d k)
    (tri (lambda ()
           (if (= k 1) (fd d) (leg d k))))
)

; leg用来画一个角
(define (leg d k)
    (sier (/ d 2) (- k 1))
    (penup)
    (fd d)
    (pendown)
)

(sier 200 3)
