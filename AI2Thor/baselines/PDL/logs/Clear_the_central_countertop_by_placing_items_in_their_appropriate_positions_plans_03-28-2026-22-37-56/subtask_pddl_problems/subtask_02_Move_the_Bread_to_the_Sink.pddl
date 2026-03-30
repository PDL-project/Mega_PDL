```pddl
(define (problem move-bread-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    sink - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location bread countertop)
    (at-location sink floor)
    (is-sink sink)
  )

  (:goal (and
    (at-location bread sink)
  ))
)
```