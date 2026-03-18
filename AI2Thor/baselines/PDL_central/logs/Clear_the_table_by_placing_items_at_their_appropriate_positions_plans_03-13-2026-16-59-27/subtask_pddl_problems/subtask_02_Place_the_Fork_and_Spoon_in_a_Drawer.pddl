```pddl
(define (problem place-fork-and-spoon-in-drawer)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    spoon - object
    drawer1 - object
    diningtable - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location fork diningtable)
    (at-location spoon diningtable)
    (at-location drawer1 floor)

    (object-close robot1 drawer1)

    (not (holding robot1 fork))
    (not (holding robot1 spoon))
  )

  (:goal (and
    (at-location fork drawer1)
    (at-location spoon drawer1)
    (object-close robot1 drawer1)
  ))
)
```