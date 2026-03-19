(define (problem clean-mug)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    sink - object
    countertop - object
    floor - object
    sinkbasin - object
    faucet - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)

    (at-location mug countertop)
    (at-location sink floor)

    (is-sink sinkbasin)
    (is-faucet faucet)
    (not (faucet-on faucet))

    (not (holding robot1 mug))
  )

  (:goal (and
    (cleaned robot1 mug)
    (at-location mug countertop)
  ))

  (:metric minimize (total-cost))
)