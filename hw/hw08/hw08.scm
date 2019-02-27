(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s))
)

(define (sign x)
  'YOUR-CODE-HERE
  (cond
    ((< x 0) -1)
    ((> x 0) 1)
    (else 0))
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
  (cond
    ((= n 0) 1)
    ((even? n) (square (pow b (/ n 2))))
    (else (* b
            (square (pow b (/ (- n 1) 2))))))
)

(define (ordered? s)
  'YOUR-CODE-HERE
  (cond
    ((null? s) True)
    ((= (length s) 1) True)
    (else (and (<= (car s) (car (cdr s))) (ordered? (cdr s)))))
)

(define (nodots s)
  'YOUR-CODE-HERE
  (if (null? s)
    nil
    (if (not (pair? s))
      (cons s nil)
      (if (pair? (car s))
        (cons (nodots (car s)) (nodots (cdr s)))
        (cons (car s) (nodots (cdr s))))))
)

(define (nodots2 s)
  (cond
    ((null? s) nil)
    ((not (pair? s)) (cons s nil))
    ((pair? (car s))
      (cons (nodots2 (car s)) (nodots2 (cdr s))))
    (else (cons (car s) (nodots2 (cdr s)))))
)



; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((> (car s) v) #f)
          ((= (car s) v) #t)
          (else (contains? (cdr s) v)))
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((contains? s v) s)
          ((< v (car s)) (cons v s))
          (else (cons (car s) (add (cdr s) v))))
)

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          (( = (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          ((> (car s) (car t)) (intersect s (cdr t))))
)

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t)))))
)

; Equivalent Python code

; def union(s, t):
;     if empty(s):
;         return t
;     elif empty(t):
;         return s
;     else:
;         e1, e2 = s.first, t.first
;         if e1 == e2:
;             return Link(e1, union2(s.rest, t.rest))
;         elif e1 < e2:
;             return Link(e1, union2(s.rest, t))
;         elif e2 < e1:
;             return Link(e2, union2(s, t.rest))
