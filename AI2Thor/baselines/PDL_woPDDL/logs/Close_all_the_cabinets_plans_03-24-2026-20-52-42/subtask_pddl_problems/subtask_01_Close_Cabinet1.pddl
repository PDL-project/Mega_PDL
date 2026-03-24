```pddl
(define (problem close-cabinet1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cabinet1 floor)
    (object-open robot1 cabinet1)
  )

  (:goal (and
    (object-close robot1 cabinet1)
  ))
)
```