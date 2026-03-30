```pddl
(define (problem open-drawer9)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer9 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location drawer9 floor)
    (object-close robot1 drawer9)
  )

  (:goal (and
    (object-open robot1 drawer9)
  ))
)
```