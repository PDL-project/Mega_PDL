```pddl
(define (problem put-spoon-in-drawer3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spoon - object
    drawer3 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location spoon countertop)
    (at-location drawer3 floor)
    (object-close robot1 drawer3)
  )

  (:goal (and
    (at-location spoon drawer3)
    (object-close robot1 drawer3)
  ))
)
```