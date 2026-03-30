(define (problem place-mug-in-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    sinkbasin1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 mug)
    (is-sink sinkbasin1)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location mug sinkbasin1)
  ))

  (:metric minimize (total-cost))
)