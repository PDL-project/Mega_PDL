(define (problem open-drawer4)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer4 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location drawer4 floor)
    ;; Removed (object-close robot1 drawer4) because it conflicts with the goal of opening the drawer
  )

  (:goal (and
    (object-open robot1 drawer4)
  ))

  (:metric minimize (total-cost))
)