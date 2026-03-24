(define (problem turn-off-faucet)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    faucet - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location faucet floor)
    (switch-on robot1 faucet)
    (is-faucet faucet)
    (faucet-on)
  )

  (:goal (and
    (switch-off robot1 faucet)
    (not (faucet-on))
  ))
)