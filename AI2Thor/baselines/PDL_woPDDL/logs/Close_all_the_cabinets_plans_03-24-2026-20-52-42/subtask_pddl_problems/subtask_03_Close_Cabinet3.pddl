```pddl
(define (problem close-cabinet3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet3 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (at-location cabinet3 floor)
    (object-open robot1 cabinet3)
  )

  (:goal (and
    (object-close robot1 cabinet3)
  ))
)
```