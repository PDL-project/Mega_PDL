```pddl
(define (problem move-bread-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    sink - object
    kitchen - object
    countertop - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location bread countertop)
    (not (holding robot1 bread))
  )

  (:goal (and
    (at-location bread sink)
  ))
)
```