(define (problem put-plate-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    plate - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 countertop)
    (at-location plate countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (holding robot1 plate))
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location plate fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)