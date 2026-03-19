(define (problem clean-mug)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    sink - object
    faucet - object
    countertop1 - object
    cabinet1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location mug countertop1)
    (at-location sink kitchen)
    (at-location faucet kitchen)
    (at-location cabinet1 kitchen)

    (is-sink sink)
    (faucet-on)

    (object-close robot1 cabinet1)
  )

  (:goal (and
    (cleaned robot1 mug)
    (at-location mug cabinet1)
    (object-close robot1 cabinet1)
  ))

  (:metric minimize (total-cost))
)