(define (problem place-fork-on-diningtable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    diningtable1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 fork)
    (at-location diningtable1 kitchen)
  )

  (:goal (and
    (at-location fork diningtable1)
    (hand-empty robot1)
  ))

  (:metric minimize (total-cost))
)