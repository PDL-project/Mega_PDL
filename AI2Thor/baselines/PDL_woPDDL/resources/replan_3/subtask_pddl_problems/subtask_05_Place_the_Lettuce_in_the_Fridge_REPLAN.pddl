```pddl
(define (problem place-lettuce-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    fridge - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 lettuce)
    (at-location fridge kitchen)

    (is-fridge fridge)
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location lettuce fridge)
    (object-close robot1 fridge)
  ))
)
```