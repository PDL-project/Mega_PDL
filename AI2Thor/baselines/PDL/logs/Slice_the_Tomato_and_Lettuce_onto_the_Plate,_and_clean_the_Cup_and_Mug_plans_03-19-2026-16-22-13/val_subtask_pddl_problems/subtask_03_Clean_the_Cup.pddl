(define (problem clean-the-cup)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cup - object
    sink - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cup floor)
    (at-location sink floor)
    (not (holding robot1 cup))
  )

  (:goal (and
    (cleaned robot1 cup)
  ))

  (:metric minimize (total-cost))
)