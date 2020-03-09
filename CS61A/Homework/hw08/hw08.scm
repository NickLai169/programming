(define (reverse lst)
    (if (null? lst) nil


        (if (null? (cdr lst))
            (cons (car lst) nil)

            (append (reverse (cdr lst)) (cons (car lst) nil))
        )
    )
)

; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
    (if (null? lst)
        nil

        (if (< x (car lst))
            (append (cons (car lst) nil) (larger-values x (cdr lst)))

            (larger-values x (cdr lst))
        )
    )
)

(define (longest-increasing-subsequence lst)
    ; the following skeleton is optional, remove if you like
    (if (null? lst)
        nil

        (begin
            (define first (car lst))
            (define rest (cdr lst))
            (define large-values-rest
                (larger-values first rest))

            (define with-first
                (append (cons (car lst) nil) (longest-increasing-subsequence large-values-rest))
            )

            (define without-first
                (longest-increasing-subsequence rest)
            )

            (if (> (length with-first) (length without-first))
                with-first
                without-first
            )
        )
    )
)




(define (cadr s) (car (cdr s)))
(define (caddr s) (cadr (cdr s)))


; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
    (if (null? expr)
        0
        
        (make-sum (derive (car expr) var) (derive-sum (cdr expr) var))
    )
)




(define (derive-product expr var)
  (define m1 (car (cdr expr)))
  (define m2 (car (cdr (cdr expr))))

  (if (number? m1)
    (define a1 m1)

    (define a1 (derive m1 var))
  )
  (if (number? m2)
    (define a2 m2)

    (define a2 (derive m2 var))
  )

    (cond
    ((and (number? m1) (number? m2))
      (define option 1)
      0
    )
    ((and (not (number? m1)) (not (number? m2)))
      (define option 2)
      (make-sum (make-product a1 m2) (make-product a2 m1))
    )
    (else
      (define option 3)
      (make-product a1 a2)
    )
  )
)

; Exponentiations are represented as lists that start with ^.
(define (power-number num pow)
    (if (= pow 0)
        1
    
        (* num (power-number num (- pow 1)))
    )
)

(define (make-exp base exponent)
    (if (number? base)
        (power-number base exponent)
        
        (if (= exponent 1)
            base
            
            (if (= exponent 0)
                1
                
                (cons '^ (cons base (cons exponent nil)))
            )
        )
    )
)

(define (base exp)
  (car (cdr exp))
)

(define (exponent exp)
  (car (cdr (cdr exp)))
)

(define (exp? exp)
    (if (list? exp)
        (eq? '^ (car exp))
        
        #f
    )
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
    
    (cond
        ((= (exponent exp) 0)
            1
        )
        ((number? (base exp))
            (power-number (base exp) (exponent exp))
        )
        
        (else
            (make-product (exponent exp) (make-exp (base exp) (- (exponent exp) 1)))
        )
    )
)
