```pddl
(define (problem wash-the-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    sink - object
    countertop - object
    faucet - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 countertop)
    (hand-empty robot1)
    (at-location bowl countertop)
    (at-location sink floor)
    (is-sink sink)
    (is-faucet faucet)
    (faucet-on)
  )

  (:goal (and
    (cleaned robot1 bowl)
    (at-location bowl countertop)
  ))
)
```