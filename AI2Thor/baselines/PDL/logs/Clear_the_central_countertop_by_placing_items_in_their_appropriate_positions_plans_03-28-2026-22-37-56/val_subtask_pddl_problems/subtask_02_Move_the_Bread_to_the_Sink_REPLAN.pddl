(define (problem move-bread-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    sinkbasin1 - object
    countertop1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location bread countertop1)
    (at-location sinkbasin1 floor)
    (is-sink sinkbasin1)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location bread sinkbasin1)
  ))

  (:metric minimize (total-cost))
)