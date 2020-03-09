(define (f f g)
  (define zipper
    (lambda (x)
      (lambda (y a)
        (x (y (f (g a))))
      )
    )
  )

  ((zipper (lambda (p) (+ p 1))) (lambda (q) (* q 2)) 9)
)
