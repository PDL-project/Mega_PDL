```lisp
(define (problem put-peppershaker-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    fridge - object
    counterTop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pepperShaker counterTop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 pepperShaker))
  )

  (:goal (and
    (at-location pepperShaker fridge)
    (not (fridge-open fridge))
  ))
)
```