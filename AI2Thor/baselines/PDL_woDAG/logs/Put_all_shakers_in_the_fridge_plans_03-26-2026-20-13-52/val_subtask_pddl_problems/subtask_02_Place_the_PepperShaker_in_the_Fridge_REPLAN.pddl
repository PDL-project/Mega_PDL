(define (problem place-peppershaker-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    fridge - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 pepperShaker)
    (at-location fridge kitchen)

    (is-fridge fridge)
    (not (fridge-open fridge))
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location pepperShaker fridge)
    (object-close robot1 fridge)
  ))

  (:metric minimize (total-cost))
)