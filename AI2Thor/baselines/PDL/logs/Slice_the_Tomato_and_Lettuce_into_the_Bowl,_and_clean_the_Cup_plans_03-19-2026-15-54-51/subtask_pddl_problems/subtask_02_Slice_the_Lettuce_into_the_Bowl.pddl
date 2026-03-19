```pddl
(define (problem slice-lettuce-into-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    lettuce - object
    bowl - object
    fridge - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location knife countertop)
    (at-location lettuce fridge)
    (at-location bowl countertop)

    (is-fridge fridge)
    (not (fridge-open fridge))

    (not (holding robot1 knife))
    (not (holding robot1 lettuce))
  )

  (:goal (and
    (sliced lettuce)
    (at-location lettuce bowl)
  ))
)
```