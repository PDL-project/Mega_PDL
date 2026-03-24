```lisp
(define (problem close-cabinet4)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet4 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cabinet4 floor)
    (object-open robot1 cabinet4)
  )

  (:goal (and
    (object-close robot1 cabinet4)
  ))
)
```