;; Scheme ;;

; Q3
(define (over-or-under x y)
  (cond
    ((> x y) 1)
    ((< x y) -1)
    [else 0])
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

; Q4
(define (filter-lst f lst)
  (if (not (null? lst))
    (if (f (car lst))
      (cons (car lst) (filter-lst f (cdr lst)))

      (filter-lst f (cdr lst))
      )
  nil)
  )

(filter-lst smol (list 2 4 6 8 10 12 14 16))

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

; Q5
(define (make-adder num)
  (define (pluser num2) (+ num2 num))
  pluser
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13
