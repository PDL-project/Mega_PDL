(define (problem clean-the-cup)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cup - object
    sink - object
    faucet - object
    floor - object
    countertop - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location cup floor)
    (at-location sink floor)
    (at-location faucet floor)
    (at-location countertop floor)

    (is-sink sink)
    (is-faucet faucet)
    (not (holding robot1 cup))
    (not (faucet-on))
  )

  (:goal (and
    (cleaned robot1 cup)
    (at-location cup countertop)
  ))

  (:metric minimize (total-cost))
)