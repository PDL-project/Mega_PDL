(define (problem place-lettuce-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    fridge - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 fridge)
    (holding robot1 lettuce)
    (is-fridge fridge)
    (object-close robot1 fridge)
  )

  (:goal (and
    (at-location lettuce fridge)
    (not (holding robot1 lettuce))
    (object-close robot1 fridge)
  ))

  (:metric minimize (total-cost))
)