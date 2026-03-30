(define (problem place-lettuce-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    fridge - object
    diningtable - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location lettuce diningtable)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location lettuce fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)