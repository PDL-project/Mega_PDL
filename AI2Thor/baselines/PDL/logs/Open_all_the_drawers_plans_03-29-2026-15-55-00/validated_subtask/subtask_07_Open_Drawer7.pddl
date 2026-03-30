(define (problem open-drawer7)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer7 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location drawer7 floor)
    (object-close robot1 drawer7)
    (= (total-cost) 0)
  )

  (:goal (and
    (object-open robot1 drawer7)
  ))

  (:metric minimize (total-cost))
)