```pddl
(define (problem slice-lettuce)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    lettuce - object
    fridge - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location knife countertop)
    (at-location lettuce fridge)
    (at-location fridge kitchen)
    (at-location countertop kitchen)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 knife))
    (not (holding robot1 lettuce))
  )

  (:goal (and
    (sliced lettuce)
    (at-location lettuce countertop)
    (not (fridge-open fridge))
  ))
)
```