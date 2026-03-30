```pddl
(define (problem put-bread-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    fridge - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location bread countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location bread fridge)
    (not (fridge-open fridge))
  ))
)
```