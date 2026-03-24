```pddl
(define (problem wash-the-pot)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pot - object
    sink - object
    faucet - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pot countertop)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (not (holding robot1 pot))
    (not (faucet-on))
  )

  (:goal (and
    (cleaned robot1 pot)
    (at-location pot countertop)
  ))
)
```