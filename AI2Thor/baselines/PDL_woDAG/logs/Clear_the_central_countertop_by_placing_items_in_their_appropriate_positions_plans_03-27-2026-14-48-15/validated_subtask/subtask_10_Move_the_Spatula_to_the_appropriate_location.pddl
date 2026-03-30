(define (problem move-spatula-to-drawer)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    drawer3 - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location spatula countertop)
    (at-location drawer3 floor)
    (object-close robot1 drawer3)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location spatula drawer3)
    (object-close robot1 drawer3)
  ))

  (:metric minimize (total-cost))
)