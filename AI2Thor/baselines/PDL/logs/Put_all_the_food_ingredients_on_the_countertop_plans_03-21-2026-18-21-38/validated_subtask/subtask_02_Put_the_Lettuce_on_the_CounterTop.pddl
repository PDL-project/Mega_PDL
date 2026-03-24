(define (problem put-lettuce-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    fridge - object
    countertop - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location lettuce fridge)
    (at-location fridge floor)
    (at-location countertop floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 lettuce))
    (object-close robot1 fridge)
  )

  (:goal (and
    (at-location lettuce countertop)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)