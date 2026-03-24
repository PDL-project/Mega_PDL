(define (problem close-cabinet8)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet8 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cabinet8 floor)
    (object-open robot1 cabinet8)
  )

  (:goal (and
    (object-close robot1 cabinet8)
  ))

  (:metric minimize (total-cost))
)