(define (problem clean-the-mug)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    sink - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location mug countertop)
    (at-location sink floor)
    (not (holding robot1 mug))
  )

  (:goal (and
    (cleaned robot1 mug)
    (at-location mug countertop)
  ))

  (:metric minimize (total-cost))
)