```pddl
(define (problem put-potato-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location potato countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 potato))
  )

  (:goal (and
    (at-location potato fridge)
    (not (fridge-open fridge))
  ))
)
```