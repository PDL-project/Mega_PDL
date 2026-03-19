(define (problem clean-mug)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    sink - object
    faucet - object
    countertop - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location mug countertop)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (is-faucet faucet)
    (not (faucet-on))
    (not (holding robot1 mug))
  )

  (:goal (and
    (cleaned robot1 mug)
    (at-location mug countertop)
  ))

  (:metric minimize (total-cost))
)