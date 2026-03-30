(define (problem wash-pot-in-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pot - object
    sinkbasin1 - object
    kitchen - object
    faucet - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 pot)
    (at-location sinkbasin1 floor)
    (is-sink sinkbasin1)
    (is-faucet faucet)
    (faucet-on)
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 pot)
  ))

  (:metric minimize (total-cost))
)