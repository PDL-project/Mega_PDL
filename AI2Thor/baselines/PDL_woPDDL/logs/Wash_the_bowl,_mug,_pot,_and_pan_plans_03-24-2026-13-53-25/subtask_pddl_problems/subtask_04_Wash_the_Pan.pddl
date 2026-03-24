```pddl
(define (problem wash-pan)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pan - object
    sink - object
    faucet - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pan countertop)
    (at-location sink floor)
    (at-location faucet floor)
    (is-sink sink)
    (not (holding robot1 pan))
    (not (faucet-on))
  )

  (:goal (and
    (cleaned robot1 pan)
    (at-location pan countertop)
  ))
)
```