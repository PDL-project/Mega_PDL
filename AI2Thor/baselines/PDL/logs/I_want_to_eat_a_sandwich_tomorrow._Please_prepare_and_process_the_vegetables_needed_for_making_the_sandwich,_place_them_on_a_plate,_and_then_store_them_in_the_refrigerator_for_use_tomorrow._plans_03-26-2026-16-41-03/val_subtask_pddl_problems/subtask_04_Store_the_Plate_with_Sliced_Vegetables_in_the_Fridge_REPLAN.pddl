(define (problem store-plate-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    plate1 - object
    fridge - object
    countertop1 - object
    kitchen - object
    lettuce - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 lettuce)
    (at-location plate1 countertop1)
    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 plate1))
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location plate1 fridge)
    (object-close robot1 fridge)
  ))

  (:metric minimize (total-cost))
)