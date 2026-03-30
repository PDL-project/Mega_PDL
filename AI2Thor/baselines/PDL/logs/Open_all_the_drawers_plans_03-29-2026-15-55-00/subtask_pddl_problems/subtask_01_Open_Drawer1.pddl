```lisp
(define (problem open-drawer1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location drawer1 floor)
    (object-close robot1 drawer1)
  )

  (:goal (and
    (object-open robot1 drawer1)
  ))
)
```