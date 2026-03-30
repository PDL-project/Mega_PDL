```pddl
(define (problem wash-the-mug)
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
    (hand-empty robot1)

    (at-location mug countertop)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (is-faucet faucet)
    (not (faucet-on))
  )

  (:goal (and
    (cleaned robot1 mug)
    (at-location mug countertop)
  ))
)
```