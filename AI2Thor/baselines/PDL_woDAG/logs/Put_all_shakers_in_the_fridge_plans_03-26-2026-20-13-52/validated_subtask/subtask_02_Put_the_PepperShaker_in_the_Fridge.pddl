(define (problem put-pepperShaker-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    fridge - object
    counterTop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pepperShaker counterTop)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location pepperShaker fridge)
    (not (fridge-open fridge))
  ))

  (:metric minimize (total-cost))
)