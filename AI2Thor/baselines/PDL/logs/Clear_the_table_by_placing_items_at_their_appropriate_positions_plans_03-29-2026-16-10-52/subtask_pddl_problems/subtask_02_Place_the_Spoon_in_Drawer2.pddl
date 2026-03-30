```pddl
(define (problem place-spoon-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spoon - object
    drawer2 - object
    diningtable - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location spoon diningtable)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location spoon drawer2)
    (object-close robot1 drawer2)
  ))
)
```