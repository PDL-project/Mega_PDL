```pddl
(define (problem put-spoon-in-drawer6)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spoon - object
    drawer6 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (at-location spoon countertop)
    (at-location drawer6 floor)
    (object-close robot1 drawer6)
    (not (holding robot1 spoon))
  )

  (:goal (and
    (at-location spoon drawer6)
    (object-close robot1 drawer6)
  ))
)
```