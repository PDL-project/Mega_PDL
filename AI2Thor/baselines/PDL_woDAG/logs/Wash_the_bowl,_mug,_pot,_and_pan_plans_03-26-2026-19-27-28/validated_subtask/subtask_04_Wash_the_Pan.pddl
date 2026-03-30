(define (problem wash-the-pan)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pan - object
    sink - object
    faucet - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location pan countertop)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (is-faucet faucet)
    (not (faucet-on))
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 pan)
    (at-location pan countertop)
  ))

  (:metric minimize (total-cost))
)