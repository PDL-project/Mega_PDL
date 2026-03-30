```pddl
(define (problem put-spoon-in-drawer1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spoon - object
    drawer1 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 countertop)
    (hand-empty robot1)
    (at-location spoon countertop)
    (at-location drawer1 floor)
    (object-close robot1 drawer1)
  )

  (:goal (and
    (at-location spoon drawer1)
    (object-close robot1 drawer1)
  ))
)
```