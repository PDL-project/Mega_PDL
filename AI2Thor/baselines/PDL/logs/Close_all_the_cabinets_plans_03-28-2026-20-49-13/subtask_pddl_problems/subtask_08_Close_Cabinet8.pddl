```pddl
(define (problem close-cabinet8)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet8 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location cabinet8 floor)
    (object-open robot1 cabinet8)
  )

  (:goal (and
    (object-close robot1 cabinet8)
  ))
)
```