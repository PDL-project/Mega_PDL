```lisp
(define (problem move-pen-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    diningtable - object
    sofa - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pen diningtable)
    (at-location sofa floor)
  )

  (:goal (and
    (at-location pen sofa)
  ))
)
```