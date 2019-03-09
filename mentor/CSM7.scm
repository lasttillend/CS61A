;; 1 waldo
; waldo returns #t if the symbol waldo is in a list. You may assume that the list passed in is well-formed

; scm> (waldo '(1 4 waldo))
; #t
; scm> (waldo '())
; #f
; scm> (waldo '(1 4 9))
; #f

(define (waldo lst)
    (if (null? lst)
        #f
        (if (eq? (car lst) 'waldo)
            #t
            (waldo (cdr lst)))))

;; 2 Extra challenge
; Define waldo so that it returns the index of the list where the symbol was found (if waldo is not in the list, return #f).

; scm> (waldo '(1 4 waldo))
; 2
; scm> (waldo '())
; #f
; scm> (waldo '(1 4 9))
; #f

(define (waldo lst)
    (define (find-waldo lst ind)
        (if (null? lst)
            #f
            (if (eq? (car lst) 'waldo)
                ind
                (find-waldo (cdr lst) (+ ind 1)))))
    (find-waldo lst 0))

;; 3 Quicksort

; scm> (quicksort (list 5 2 4 3 12 7))
; (2 3 4 5 7 12)

; my solution(ugly but works)
(define (partition pivot lst)
        (if (null? lst)
            (cons nil nil)
            (begin
                (define p (partition pivot (cdr lst)))
                (define less (car p))
                (define greater (cdr p))
                (if (< (car lst) pivot)
                    (cons (cons (car lst) less) greater)
                    (cons less (cons (car lst) greater))))))

(define (quicksort lst)
    (if (null? lst)
        nil
        (begin
            (define pivot (car lst))
            (define p (partition pivot (cdr lst)))
            (define less-sort (quicksort (car p)))
            (define greater-sort (quicksort (cdr p)))
            (append less-sort (list pivot) greater-sort))))

; Method 2 (elegant!)
(define (filter-comp comp pivot s)
    (filter (lambda (x) (comp x pivot)) s))

(define (quick-sort s)
    (if (<= (length s) 1)
        s
        (let ((pivot (car s)))
            (append (quick-sort (filter-comp < pivot s))
                (filter-comp = pivot s)
                (quick-sort (filter-comp > pivot s))))))
