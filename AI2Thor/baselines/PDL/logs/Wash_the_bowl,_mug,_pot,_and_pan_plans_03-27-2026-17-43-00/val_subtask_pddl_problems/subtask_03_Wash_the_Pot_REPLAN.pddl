(define (problem wash-pot)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pot - object
    faucet - object
    sink - object
    countertop3 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location pot countertop3)
    (at-location faucet floor)
    (at-location sink floor)

    (is-faucet faucet)
    (faucet-on)
    (is-sink sink)
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 pot)
  ))

  (:metric minimize (total-cost))
)