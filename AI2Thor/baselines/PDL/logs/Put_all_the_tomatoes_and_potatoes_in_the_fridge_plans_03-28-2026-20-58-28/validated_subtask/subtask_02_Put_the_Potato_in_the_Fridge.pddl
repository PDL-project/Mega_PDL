(define (problem put-potato-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    fridge - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location potato countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location potato fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)