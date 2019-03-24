; 1. Implement double_naturals, which is a stream that evaluates to the sequence 1, 1, 2, 2, 3, 3 et.
(define (double_naturals)
    (double_naturals-helper 1 #f))

(define (double_naturals-helper first go-next)
    (if go-next
        (cons-stream first
                     (double_naturals-helper (+ first 1 ) #f))
        (cons-stream first
                     (double_naturals-helper first #t))))

; 2. Implement interleave, which returns a stream that alternates between the values in stream1 and stream2. Assume that the streams are infinitely long.)
(define (interleave stream1 stream2)
    (interleave-helper stream1 stream2 #t))

(define (interleave-helper stream1 stream2 first?)
    (if first?
        (cons-stream (car stream1)
                     (interleave-helper (cdr-stream stream1)
                                        stream2
                                        #f))
        (cons-stream (car stream2)
                     (interleave-helper stream1
                                        (cdr-stream stream2)
                                        #t))))
