(define (problem put-bowl-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 countertop)
    (at-location bowl countertop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (holding robot1 bowl))
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location bowl fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)