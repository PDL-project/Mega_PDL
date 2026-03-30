```lisp
(define (problem close-cabinet6)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet6 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location cabinet6 floor)
    (object-open robot1 cabinet6)
  )

  (:goal (and
    (object-close robot1 cabinet6)
  ))
)
```