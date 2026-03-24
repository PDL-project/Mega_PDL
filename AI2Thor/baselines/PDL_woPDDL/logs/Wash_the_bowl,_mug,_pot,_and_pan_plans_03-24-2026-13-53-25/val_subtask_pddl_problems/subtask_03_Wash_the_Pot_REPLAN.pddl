(define (problem wash-pot)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pot - object
    faucet - object
    sink - object
    countertop3 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location pot countertop3)
    (at-location faucet floor)
    (at-location sink floor)
    (is-sink sink)
    (is-faucet faucet)
    (faucet-on)
    (not (holding robot1 pot))
  )

  (:goal (and
    (cleaned robot1 pot)
  ))

  (:metric minimize (total-cost))
)