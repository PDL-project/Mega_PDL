```pddl
(define (problem open-drawer8)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer8 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location drawer8 floor)
    (object-close robot1 drawer8)
  )

  (:goal (and
    (object-open robot1 drawer8)
  ))
)
```