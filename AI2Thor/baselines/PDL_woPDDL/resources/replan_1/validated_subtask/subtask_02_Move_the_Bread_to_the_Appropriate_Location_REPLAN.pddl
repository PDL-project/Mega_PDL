(define (problem move-bread-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    sink - object
    kitchen - object
    countertop - object
    faucet - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location bread countertop)
    (not (holding robot1 bread))
    (is-sink sink)
    (is-faucet faucet)
    (not (faucet-on))
  )

  (:goal (and
    (at-location bread sink)
  ))

  (:metric minimize (total-cost))
)