```pddl
(define (problem put-lettuce-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location lettuce countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location lettuce fridge)
    (not (fridge-open fridge))
  ))
)
```