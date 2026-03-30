(define (problem put-bread-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    fridge - object
    kitchen - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location bread countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location bread fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)