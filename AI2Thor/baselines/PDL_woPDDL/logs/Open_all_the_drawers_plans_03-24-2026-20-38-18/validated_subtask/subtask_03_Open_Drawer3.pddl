(define (problem open-drawer3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer3 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location drawer3 floor)
    ;; Removed (object-close robot1 drawer3) because it conflicts with the goal of opening the drawer
  )

  (:goal (and
    (object-open robot1 drawer3)
  ))

  (:metric minimize (total-cost))
)