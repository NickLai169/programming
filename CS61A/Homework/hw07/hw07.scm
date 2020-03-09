(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond
    ((> x 0) 1)
    ((< x 0) -1)
    [else 0])
)

(define (square x) (* x x))

(define (pow b n)
  (if (= n 1)
    b

    (if (even? n)
      (* (pow b (quotient n 2)) (pow b (quotient n 2)))

      (* (pow b (- n 1)) b)
      )
    )
  )

(define (ordered? s)
  (if (or (null? (cdr s)) (null? s))
    #t

    (if (> (car s) (car (cdr s)))
      #f

      (ordered? (cdr))
      )
    )
)
