(define (problem wash-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    sink - object
    faucet - object
    countertop - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location bowl countertop)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (is-faucet faucet)
    (not (faucet-on))
    (= (total-cost) 0)
  )

  (:goal (and
    (cleaned robot1 bowl)
    (at-location bowl countertop)
  ))

  (:metric minimize (total-cost))
)