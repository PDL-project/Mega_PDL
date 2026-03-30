(define (problem move-mug-to-countertop2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    bread - object
    countertop2 - object
    current_position_of_robot3 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 current_position_of_robot3)
    (holding robot1 bread)
    (at-location mug current_position_of_robot3)
    (at-location countertop2 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location mug countertop2)
  ))

  (:metric minimize (total-cost))
)