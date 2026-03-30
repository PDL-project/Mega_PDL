(define (problem place-tomato-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    fridge - object
    diningTable - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location tomato diningTable)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location tomato fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)