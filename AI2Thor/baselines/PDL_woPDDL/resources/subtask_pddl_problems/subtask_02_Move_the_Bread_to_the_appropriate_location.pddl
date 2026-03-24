```lisp
(define (problem move-bread-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    countertop - object
    sink - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location bread countertop)
    (at-location sink floor)
    (not (holding robot1 bread))
  )

  (:goal (and
    (at-location bread sink)
    (not (holding robot1 bread))
  ))
)
```