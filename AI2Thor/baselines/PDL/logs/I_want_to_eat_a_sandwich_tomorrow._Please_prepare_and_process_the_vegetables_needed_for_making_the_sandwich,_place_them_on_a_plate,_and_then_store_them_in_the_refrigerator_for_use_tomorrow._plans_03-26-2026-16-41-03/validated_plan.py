(define (problem slice-lettuce)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    lettuce - object
    fridge - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location knife countertop)
    (at-location lettuce fridge)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 knife))
    (not (holding robot1 lettuce))
    (= (total-cost) 0)
  )

  (:goal (and
    (sliced lettuce)
    (at-location lettuce countertop)
  ))

  (:metric minimize (total-cost))
)