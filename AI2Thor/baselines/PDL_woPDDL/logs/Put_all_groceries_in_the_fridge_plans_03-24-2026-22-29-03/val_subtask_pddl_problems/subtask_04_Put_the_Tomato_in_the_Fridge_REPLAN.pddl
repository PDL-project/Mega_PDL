(define (problem put-tomato-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    fridge - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 fridge)
    (holding robot1 tomato)

    (is-fridge fridge)
    (object-close robot1 fridge)
  )

  (:goal (and
    (at-location tomato fridge)
    (object-close robot1 fridge)
  ))

  (:metric minimize (total-cost))
)