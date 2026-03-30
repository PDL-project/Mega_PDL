(define (problem open-drawer4)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer4 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location drawer4 floor)
    (object-close robot1 drawer4)
    (= (total-cost) 0)
  )

  (:goal (and
    (object-open robot1 drawer4)
  ))

  (:metric minimize (total-cost))
)