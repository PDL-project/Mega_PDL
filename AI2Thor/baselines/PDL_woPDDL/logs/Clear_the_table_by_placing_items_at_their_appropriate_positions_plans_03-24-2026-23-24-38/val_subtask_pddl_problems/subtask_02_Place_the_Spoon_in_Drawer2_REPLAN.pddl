(define (problem place-spoon-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spoon - object
    drawer2 - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 spoon)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location spoon drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)