```pddl
(define (problem move-fork-to-drawer)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    drawer2 - object
    counterTop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location fork counterTop)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
    (not (holding robot1 fork))
  )

  (:goal (and
    (at-location fork drawer2)
    (object-close robot1 drawer2)
  ))
)
```