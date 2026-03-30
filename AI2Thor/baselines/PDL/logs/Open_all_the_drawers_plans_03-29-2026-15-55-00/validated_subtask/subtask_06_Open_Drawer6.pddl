(define (problem open-drawer6)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer6 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location drawer6 floor)
    (object-close robot1 drawer6)
    (= (total-cost) 0)
  )

  (:goal (and
    (object-open robot1 drawer6)
  ))

  (:metric minimize (total-cost))
)