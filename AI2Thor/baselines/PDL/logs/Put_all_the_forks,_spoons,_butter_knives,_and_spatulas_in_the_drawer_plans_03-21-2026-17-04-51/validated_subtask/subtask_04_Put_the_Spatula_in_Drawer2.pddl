(define (problem put-spatula-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    drawer2 - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location spatula countertop)
    (at-location drawer2 floor)

    (object-close robot1 drawer2)
    (not (holding robot1 spatula))
  )

  (:goal (and
    (at-location spatula drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)