(define (problem put-vase2-on-countertop2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    vase2 - object
    shelf - object
    countertop2 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location vase2 shelf)
    (not (holding robot1 vase2))
    (not (object-close robot1 shelf)) ;; Ensure shelf is openable
  )

  (:goal (and
    (at-location vase2 countertop2)
  ))

  (:metric minimize (total-cost))
)