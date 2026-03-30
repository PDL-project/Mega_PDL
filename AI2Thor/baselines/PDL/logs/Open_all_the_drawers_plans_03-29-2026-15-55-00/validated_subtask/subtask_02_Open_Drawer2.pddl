(define (problem open-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer2 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
    (= (total-cost) 0)
  )

  (:goal (and
    (object-open robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)