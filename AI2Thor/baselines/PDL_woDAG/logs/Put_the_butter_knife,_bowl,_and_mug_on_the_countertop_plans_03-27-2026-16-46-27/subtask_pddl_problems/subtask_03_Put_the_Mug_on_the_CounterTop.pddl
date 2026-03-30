```lisp
(define (problem put-mug-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    countertop3 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location mug floor)
    (at-location countertop3 floor)
  )

  (:goal (and
    (at-location mug countertop3)
  ))
)
```