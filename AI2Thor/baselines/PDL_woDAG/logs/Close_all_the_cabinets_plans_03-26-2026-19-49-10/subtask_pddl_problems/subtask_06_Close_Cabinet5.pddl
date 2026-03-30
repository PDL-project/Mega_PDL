```lisp
(define (problem close-cabinet5)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet5 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location cabinet5 floor)
    (object-open robot1 cabinet5)
  )

  (:goal (and
    (object-close robot1 cabinet5)
  ))
)
```