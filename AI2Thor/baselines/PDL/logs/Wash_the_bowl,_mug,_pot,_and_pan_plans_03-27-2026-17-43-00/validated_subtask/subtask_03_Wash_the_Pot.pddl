(define (problem wash-the-pot)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pot - object
    sink - object
    faucet - object
    countertop - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location pot countertop)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (is-faucet faucet)
    (not (faucet-on))
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 pot)
    (at-location pot countertop)
  ))

  (:metric minimize (total-cost))
)