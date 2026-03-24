(define (problem place-remotecontrol)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remoteControl - object
    armchair1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 remoteControl)
    (not (object-close robot1 armchair1))
  )

  (:goal (and
    (at-location remoteControl armchair1)
  ))

  (:metric minimize (total-cost))
)