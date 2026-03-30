(define (problem put-spatula-in-drawer5)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    drawer5 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location spatula countertop)
    (at-location drawer5 floor)
    (object-close robot1 drawer5)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location spatula drawer5)
    (object-close robot1 drawer5)
  ))

  (:metric minimize (total-cost))
)