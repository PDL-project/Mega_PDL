```pddl
(define (problem put-knife-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    drawer2 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location knife countertop)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location knife drawer2)
    (object-close robot1 drawer2)
  ))
)
```