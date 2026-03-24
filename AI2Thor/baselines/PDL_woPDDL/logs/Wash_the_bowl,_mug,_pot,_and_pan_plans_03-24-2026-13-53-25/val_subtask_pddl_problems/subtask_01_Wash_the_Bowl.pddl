(define (problem wash-the-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    sink - object
    faucet - object
    countertop - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location bowl countertop)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (is-faucet faucet)
    (not (faucet-on))
    (not (holding robot1 bowl))
  )

  (:goal (and
    (cleaned robot1 bowl)
    (at-location bowl countertop)
  ))

  (:metric minimize (total-cost))
)