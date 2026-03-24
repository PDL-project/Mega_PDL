(define (problem put-potato-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 countertop)
    (at-location potato countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 potato))
  )

  (:goal (and
    (at-location potato fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)