```lisp
(define (problem place-lettuce-and-tomato-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    tomato - object
    fridge - object
    diningtable - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location lettuce diningtable)
    (at-location tomato diningtable)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 lettuce))
    (not (holding robot1 tomato))
  )

  (:goal (and
    (at-location lettuce fridge)
    (at-location tomato fridge)
    (not (holding robot1 lettuce))
    (not (holding robot1 tomato))
    (object-close robot1 fridge)
  ))
)
```