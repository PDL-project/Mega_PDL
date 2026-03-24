(define (problem wash-pan)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pan - object
    sink - object
    kitchen - object
    robot3 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pan robot3)
    (is-sink sink)
    (faucet-on)
  )

  (:goal (and
    (cleaned robot1 pan)
  ))

  (:metric minimize (total-cost))
)