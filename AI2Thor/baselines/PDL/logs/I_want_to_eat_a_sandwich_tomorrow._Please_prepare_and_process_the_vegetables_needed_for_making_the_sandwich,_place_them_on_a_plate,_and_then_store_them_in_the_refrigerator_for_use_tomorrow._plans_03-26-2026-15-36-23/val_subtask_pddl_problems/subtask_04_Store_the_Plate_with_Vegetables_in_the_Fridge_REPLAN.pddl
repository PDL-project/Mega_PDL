(define (problem store-plate-with-vegetables-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    plate - object
    lettuce - object
    fridge - object
    robot3 - object
    kitchen - object
    countertop1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location plate robot3)
    (holding robot1 lettuce)
    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 plate))
    (object-close robot1 fridge)
  )

  (:goal (and
    (at-location plate fridge)
    (at-location lettuce plate)
    (object-close robot1 fridge)
  ))

  (:metric minimize (total-cost))
)