```pddl
(define (problem put-vase1-on-countertop1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    vase1 - object
    shelf1 - object
    countertop1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location vase1 shelf1)
    (not (holding robot1 vase1))
  )

  (:goal (and
    (at-location vase1 countertop1)
    (not (holding robot1 vase1))
  ))
)
```