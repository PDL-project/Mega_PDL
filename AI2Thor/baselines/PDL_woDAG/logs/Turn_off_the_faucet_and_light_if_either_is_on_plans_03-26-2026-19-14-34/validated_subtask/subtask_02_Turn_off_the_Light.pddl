(define (problem switch-off-light)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lightswitch - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location lightswitch floor)
    (switch-on robot1 lightswitch)
    (= (total-cost) 0)
  )

  (:goal (and
    (switch-off robot1 lightswitch)
  ))

  (:metric minimize (total-cost))
)