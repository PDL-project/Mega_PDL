(define (problem place-sliced-vegetables-on-plate)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    robot3 - robot
    lettuce - object
    plate - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 lettuce)
    (at robot1 robot3)
    (not (object-close robot1 plate))
  )

  (:goal (and
    (at-location lettuce plate)
    (not (holding robot1 lettuce))
  ))

  (:metric minimize (total-cost))
)