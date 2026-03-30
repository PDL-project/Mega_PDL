(define (problem clean-pan)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pan - object
    sinkbasin1 - object
    kitchen - object
    floor - object
    faucet - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 pan)
    (at-location sinkbasin1 floor)
    (is-sink sinkbasin1)
    (is-faucet faucet)
    (not (faucet-on))
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 pan)
    (hand-empty robot1)
  ))

  (:metric minimize (total-cost))
)