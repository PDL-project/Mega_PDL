(define (problem clean-mug)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    sinkbasin1 - object
    faucet - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 mug)
    (at-location sinkbasin1 floor)
    (at-location faucet floor)
    (is-sink sinkbasin1)
    (is-faucet faucet)
    (not (faucet-on))
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 mug)
    (at robot1 sinkbasin1)
  ))

  (:metric minimize (total-cost))
)