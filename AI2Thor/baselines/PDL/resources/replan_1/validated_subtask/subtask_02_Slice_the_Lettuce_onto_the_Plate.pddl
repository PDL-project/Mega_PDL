(define (problem slice-lettuce-onto-plate)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    lettuce - object
    plate - object
    fridge - object
    countertop - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location knife countertop)
    (at-location lettuce fridge)
    (at-location plate countertop)

    (is-fridge fridge)
    (not (fridge-open fridge))

    (not (holding robot1 knife))
    (not (holding robot1 lettuce))
  )

  (:goal (and
    (sliced lettuce)
    (at-location lettuce plate)
  ))

  (:metric minimize (total-cost))
)