```pddl
(define (problem put-fork-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    drawer2 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location fork countertop)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location fork drawer2)
    (object-close robot1 drawer2)
  ))
)
```