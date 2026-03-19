```pddl
(define (problem clean-mug)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    sink - object
    countertop - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 countertop)
    (at-location mug countertop)
    (is-sink sink)
    (faucet-on)
    (not (holding robot1 mug))
  )

  (:goal (and
    (cleaned robot1 mug)
    (at-location mug countertop)
  ))
)
```