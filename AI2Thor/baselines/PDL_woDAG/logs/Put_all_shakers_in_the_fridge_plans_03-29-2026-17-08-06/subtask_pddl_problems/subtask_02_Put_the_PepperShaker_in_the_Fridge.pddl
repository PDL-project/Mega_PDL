```pddl
(define (problem put-pepperShaker-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pepperShaker countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location pepperShaker fridge)
    (not (fridge-open fridge))
  ))
)
```