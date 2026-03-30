(define (problem wash-pan)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pan - object
    faucet - object
    sink - object
    countertop1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pan countertop1)
    (at-location faucet sink)
    (is-faucet faucet)
    (is-sink sink)
    (faucet-on)
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 pan)
  ))

  (:metric minimize (total-cost))
)