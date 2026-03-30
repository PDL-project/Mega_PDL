(define (problem place-sliced-lettuce-on-plate1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    plate1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 plate1)
    (holding robot1 lettuce)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location lettuce plate1)
    (not (holding robot1 lettuce))
  ))

  (:metric minimize (total-cost))
)