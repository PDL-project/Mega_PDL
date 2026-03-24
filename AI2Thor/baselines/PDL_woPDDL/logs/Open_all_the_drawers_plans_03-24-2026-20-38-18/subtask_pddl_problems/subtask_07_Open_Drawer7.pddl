```pddl
(define (problem open-drawer7)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer7 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (at-location drawer7 floor)
    (object-close robot1 drawer7)
  )

  (:goal (and
    (object-open robot1 drawer7)
  ))
)
```