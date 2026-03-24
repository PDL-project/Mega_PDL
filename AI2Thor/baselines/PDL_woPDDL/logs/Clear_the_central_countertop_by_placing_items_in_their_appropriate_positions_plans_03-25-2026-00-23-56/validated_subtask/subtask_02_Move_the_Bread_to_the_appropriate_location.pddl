(define (problem move-bread-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    countertop - object
    sink - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location bread countertop)
    (at-location sink floor)
    (not (holding robot1 bread))
    (is-sink sink)
    (not (faucet-on))
  )

  (:goal (and
    (at-location bread sink)
    (not (holding robot1 bread))
  ))

  (:metric minimize (total-cost))
)