(define (problem open-drawer9)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer9 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location drawer9 floor)
    (object-close robot1 drawer9)
  )

  (:goal (and
    (object-open robot1 drawer9)
  ))

  (:metric minimize (total-cost))
)