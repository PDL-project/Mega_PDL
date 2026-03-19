(define (problem clean-the-cup)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cup - object
    sink - object
    countertop - object
    floor - object
    sinkbasin - object
    faucet - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)

    (at-location cup floor)
    (at-location sink floor)
    (at-location countertop floor)

    (is-sink sinkbasin)
    (is-faucet faucet)
    (not (faucet-on))

    (not (holding robot1 cup))
  )

  (:goal (and
    (cleaned robot1 cup)
    (at-location cup countertop)
  ))

  (:metric minimize (total-cost))
)