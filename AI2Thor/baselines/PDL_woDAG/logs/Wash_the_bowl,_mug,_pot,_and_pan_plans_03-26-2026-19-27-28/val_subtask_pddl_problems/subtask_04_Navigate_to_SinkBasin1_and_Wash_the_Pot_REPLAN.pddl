(define (problem clean-pot)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pot - object
    sinkbasin1 - object
    faucet - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 pot)
    (at-location sinkbasin1 floor)
    (is-sink sinkbasin1)
    (is-faucet faucet)
    (not (faucet-on))
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 pot)
  ))

  (:metric minimize (total-cost))
)