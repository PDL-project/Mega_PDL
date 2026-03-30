(define (problem put-mug-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 countertop)
    (at-location mug countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (not (holding robot1 mug))
  )

  (:goal (and
    (at-location mug fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)