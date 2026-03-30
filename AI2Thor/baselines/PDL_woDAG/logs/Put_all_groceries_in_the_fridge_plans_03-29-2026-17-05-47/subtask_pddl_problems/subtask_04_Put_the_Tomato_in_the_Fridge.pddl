```pddl
(define (problem put-tomato-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    fridge - object
    kitchen - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location tomato countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location tomato fridge)
    (not (fridge-open fridge))
  ))
)
```