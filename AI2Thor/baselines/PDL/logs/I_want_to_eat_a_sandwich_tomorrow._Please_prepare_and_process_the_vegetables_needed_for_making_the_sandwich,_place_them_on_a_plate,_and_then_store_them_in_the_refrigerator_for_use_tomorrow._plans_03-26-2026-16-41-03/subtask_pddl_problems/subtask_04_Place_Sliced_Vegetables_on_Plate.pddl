```pddl
(define (problem place-sliced-vegetables-on-plate)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    plate - object
    lettuce - object
    tomato - object
    bread - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location plate countertop)
    (at-location lettuce countertop)
    (at-location tomato countertop)
    (at-location bread countertop)

    (not (holding robot1 plate))
    (not (holding robot1 lettuce))
    (not (holding robot1 tomato))
    (not (holding robot1 bread))

    (sliced lettuce)
    (sliced tomato)
  )

  (:goal (and
    (at-location lettuce plate)
    (at-location tomato plate)
    (not (holding robot1 lettuce))
    (not (holding robot1 tomato))
  ))
)
```