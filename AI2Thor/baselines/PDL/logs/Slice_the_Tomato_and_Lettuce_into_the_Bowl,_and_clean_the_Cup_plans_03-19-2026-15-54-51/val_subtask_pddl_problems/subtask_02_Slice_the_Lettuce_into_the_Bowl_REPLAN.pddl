(define (problem slice-lettuce-into-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    knife - object
    bowl1 - object
    fridge1 - object
    countertop1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location lettuce fridge1)
    (at-location knife countertop1)
    (at-location bowl1 countertop1)

    (is-fridge fridge1)
    (not (fridge-open fridge1))
    (not (holding robot1 lettuce))
    (not (holding robot1 knife))
    (object-close robot1 bowl1)
  )

  (:goal (and
    (sliced lettuce)
    (at-location lettuce bowl1)
    (object-close robot1 bowl1)
  ))

  (:metric minimize (total-cost))
)