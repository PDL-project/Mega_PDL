```lisp
(define (problem put-ladle-in-drawer3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    ladle - object
    drawer3 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location ladle countertop)
    (at-location drawer3 floor)
    (object-close robot1 drawer3)
  )

  (:goal (and
    (at-location ladle drawer3)
    (object-close robot1 drawer3)
  ))
)
```