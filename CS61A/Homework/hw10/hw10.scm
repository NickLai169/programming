(define (accumulate combiner start n term)
  (define (t-r-accumulate num terminology)
      ; (print num)
      (if (= num 1)
        1
        (combiner (terminology num) (t-r-accumulate (- num 1) terminology))
      )
  )
  (combiner start
    (t-r-accumulate n term)
  )
)

(define (accumulate-tail combiner start n term)
  (define (t-r-accumulate-tail counter currnum)
    (if (> counter n)
      currnum
      (t-r-accumulate-tail (+ counter 1) (combiner currnum (term counter)))
    )
  )
  (t-r-accumulate-tail 1 start)
)

(define (rle s)
  (define (stream-walker stream my-num counter-list)
    (if (or (null? stream) (not (= my-num (car stream))))
      counter-list
      (stream-walker (cdr-stream stream) my-num (cons my-num (cons (+ (car (cdr counter-list)) 1) nil)))
    )
  )
  (define (stream-walker-2 stream my-num)
    (if (null? stream)
      nil
      (if (= (car stream) my-num)
        (stream-walker-2 (cdr-stream stream) my-num)
        stream
      )
    )
  )
  (if (null? s)
    nil

    (cons-stream (stream-walker (cdr-stream s) (car s) (list (car s) 1)) (rle (stream-walker-2 s (car s))))
  )
)
