(define (problem wash-cup)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cup - object
    cabinet1 - object
    sinkbasin1 - object
    faucet1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location cup cabinet1)
    (at-location cabinet1 kitchen)
    (at-location sinkbasin1 kitchen)

    (object-close robot1 cabinet1)

    (is-sink sinkbasin1)
    (is-faucet faucet1)
    (not (faucet-on faucet1))

    (not (holding robot1 cup))
  )

  (:goal (and
    (cleaned robot1 cup)
    (not (holding robot1 cup))
  ))

  (:metric minimize (total-cost))
)