(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (lst) (append (list first) lst)) rests)
)

(define (zip pairs)
  (if (null? pairs) '(()())
      (list (cons (car (car pairs)) (car (zip (cdr pairs))))
	    (cons (cadr (car pairs)) (cadr (zip (cdr pairs)))))))

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (enum s index)
    (if (null? s)
	()
        (cons (list index (car s)) (enum (cdr s) (+ index 1)))))
  (enum s 0)
  )
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (cond ((> total 0) (append (if (<= (car denoms) total)
				 (cons-all (car denoms)
					   (list-change (- total (car denoms)) denoms))
				 ())
			     (if (not (null? (cdr denoms))) 
				 (list-change total (cdr denoms))
				 ())))
	((= total 0) '(())))
  )
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
	 ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append (list 'lambda params) (map let-to-lambda body))
	   ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (begin (define bindings (zip values))
		  (append (list (append (list 'lambda
					      (car bindings))
					(map let-to-lambda body))) 
			  (map let-to-lambda (cadr bindings))))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (append (list (car expr)) (map let-to-lambda (cdr expr)))
         ; END PROBLEM 19
         )))
