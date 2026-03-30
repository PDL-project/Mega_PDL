```pddl
(define (problem open-drawer5)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer5 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location drawer5 floor)
    (object-close robot1 drawer5)
  )

  (:goal (and
    (object-open robot1 drawer5)
  ))
)
```