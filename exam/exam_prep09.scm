; More Scheme, Interpreters, Streams and Macros

; 1 Scheme
; 1. non-contiguous
(define (non-contiguous subseq lst)
    (cond ((null? subseq) #t)
          ((null? lst) #f)
          ((= (car subseq) (car lst)) (non-contiguous (cdr subseq) (cdr lst)))
          (else (non-contiguous subseq (cdr lst)))))

; The above procedure is tail recursive

(define (assert-equals expected expression)
    (if (eq? (eval expression) expected)
        'OK
        `(expected ,expected but got ,(eval expression))))

; 2. directions
(define (directions n sym)
    (define (search s exp)
        ; Search an expression s for n and return an expression based on exp.
        (cond ((number? s) (if (= s n) exp nil))
              ((null? s) nil)
              (else (search-list s exp))))

    (define (search-list s exp)
        ; Search a nested list s for n and return an expression based on exp.
        (let ((first (search (car s) (list 'car exp)))
              (rest (search (cdr s) (list 'cdr exp))))
             (if (null? first) rest first)))

    (search (eval sym) sym))


; 2 Streams
; 1. Repeat n cycle
(define (stream-to-list s n)
    (if (or (= n 0) (null? s))
        nil
        (cons (car s)
              (stream-to-list (cdr-stream s) (- n 1)))))

(define (cycle lst n)
    (define s (cons-stream (car lst) (helper (cdr lst) n)))
    (define (helper buffer num)
        (cond ((= n 0) s)
              ((null? buffer) (helper lst (- n 1)))
              (else (cons-stream (car buffer) (helper (cdr buffer) n)))))
    s)

; 2. Stream first n
(define (stream-first n lst)
  (define (stream-helper i curr-lst)
    (if (or (= i 0) (null? curr-lst))
      (stream-first n lst)
      (cons-stream (car lst) (stream-helper (- i 1) (cdr curr-lst)))))
  (stream-helper n lst))

; 3 Macros
; Implement an OOP system is Scheme using macros

; PYTHON OOP CODE
; class Dog:
;     def age_type():
;         if Dog.a < 7:
;             return "young"
;         elif Dog.a > 7:
;             return "old"
;         else:
;             return "middle aged"
; Dog.n = "Fido"
; Dog.a = 9
; d = Dog()
; print(d.age_type())

; SCHEME OOP CODE
(define-class Dog)
(define-attr Dog n 'Fido)
(define-attr Dog a 9)
(define-method Dog (age-type)
    (cond
        ((< (get-attr Dog a) 7) 'young)
        ((> (get-attr Dog a) 9) 'old)
        (else 'middle-aged)))
(define d (construct Dog))
(print (call-method d (age-type)))

; IMPLEMENTATION
(define-macro (define-class class-name)
    `(define ,class-name nil))

(define-macro (construct class-name)
    `(quote ,class-name))

(define-macro (define-attr class-name attr-name value)
    `(define
        ,class-name
        (cons
            '(,attr-name ,(eval value))
            ,class-name)))

(define-macro (get-attr class-name attr-name)
    `(begin
        (define (helper class)
            (if (eq? (quote ,attr-name) (car (car class)))
                (car (cdr (car class)))
                (helper (cdr class))))
        (helper ,class-name)))

(define-macro (define-method class-name signature body)
    `(define-attr ,class-name ,(car signature) (lambda ,(cdr signature) ,body)))

(define-macro (call-method instance call)
    (cons `(get-attr ,(eval instance) ,(car call)) (cdr call)))
