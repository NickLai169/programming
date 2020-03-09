; Lab 13: Final Review

(define (compose-all funcs)
  (if (null? funcs)
    (begin
      (define (fugoff-mate x)
        x
      )
      fugoff-mate
    )

    (begin
      (define (reverser lst curr)
        (if (null? lst)
          curr
          (reverser (cdr lst) (cons (car lst) curr))
        )
      )

      (define (tr-compose-all fun)
        (if (null? (cdr fun))
          (begin
            (define (the-func x)
            ((car fun) x)
            )
            the-func
          )

          (begin
            (define (the-func x)
            ((car fun) ((tr-compose-all (cdr fun)) x))
            )
            the-func
          )
        )
      )

      (tr-compose-all (reverser funcs '()))
    )
  )
)

(define (compose-all-2 funcs)
  (if (null? funcs)
    (lambda (x) x)

    (lambda (x)
      ((compose-all-2 (cdr funcs)) ((car funcs) x))
    )
  )
)
