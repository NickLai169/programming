(define-macro (list-of map-expr for var in lst if filter-expr)
  `(begin
    (if (null? ,lst) nil (define ,var (car ,lst)))
      (cond
        ((null? ,lst)
          nil)
        (,filter-expr
          (cons ,map-expr (list-of ,map-expr for ,var in (cdr ,lst) if ,filter-expr)))
        (else
          (list-of ,map-expr for ,var in (cdr ,lst) if ,filter-expr))
      )
  )
)
