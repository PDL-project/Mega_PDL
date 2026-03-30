```pddl
(define (problem put-bowl-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location bowl countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location bowl fridge)
    (not (fridge-open fridge))
  ))
)
```