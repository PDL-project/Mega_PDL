```pddl
(define (problem place-lettuce-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location lettuce floor)
    (not (holding robot1 lettuce))
  )

  (:goal (and
    (at-location lettuce countertop1)
    (not (holding robot1 lettuce))
  ))
)
```