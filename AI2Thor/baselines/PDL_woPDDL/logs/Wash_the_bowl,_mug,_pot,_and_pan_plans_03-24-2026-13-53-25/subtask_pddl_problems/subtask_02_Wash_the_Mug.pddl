```pddl
(define (problem wash-mug)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    sink - object
    faucet - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location mug countertop)
    (at-location sink floor)
    (is-sink sink)
    (is-faucet faucet)
    (at-location faucet floor)
    (faucet-on)
    (not (holding robot1 mug))
  )

  (:goal (and
    (cleaned robot1 mug)
    (at-location mug countertop)
  ))
)
```