```lisp
(define (problem put-pencil-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    coffeetable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pencil coffeetable)
    (at-location sofa floor)
  )

  (:goal (and
    (at-location pencil sofa)
  ))
)
```