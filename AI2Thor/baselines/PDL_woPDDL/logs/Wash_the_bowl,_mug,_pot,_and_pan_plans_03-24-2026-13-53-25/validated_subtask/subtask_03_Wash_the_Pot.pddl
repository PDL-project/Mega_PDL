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
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 countertop)
    (at-location pot countertop)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (is-faucet faucet)
    (not (holding robot1 pot))
    (not (faucet-on))
  )

  (:goal (and
    (cleaned robot1 pot)
    (at-location pot countertop)
  ))

  (:metric minimize (total-cost))
)