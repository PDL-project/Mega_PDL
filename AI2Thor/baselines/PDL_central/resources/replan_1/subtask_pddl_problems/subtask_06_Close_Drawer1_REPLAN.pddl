```pddl
(define (problem close-drawer1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 drawer1)
    (at-location drawer1 floor)
    (object-open robot1 drawer1)
  )

  (:goal (and
    (object-close robot1 drawer1)
  ))
)
```