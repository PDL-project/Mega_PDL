```pddl
(define (problem put-saltshaker-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    saltshaker - object
    fridge - object
    kitchen - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location saltshaker countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 saltshaker))
  )

  (:goal (and
    (at-location saltshaker fridge)
    (not (fridge-open fridge))
  ))
)
```