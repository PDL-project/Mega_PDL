(define (problem put-spatula-in-drawer3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    drawer3 - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location spatula countertop)
    (at-location drawer3 floor)
    (object-close robot1 drawer3)
    (not (holding robot1 spatula))
  )

  (:goal (and
    (at-location spatula drawer3)
    (object-close robot1 drawer3)
  ))

  (:metric minimize (total-cost))
)