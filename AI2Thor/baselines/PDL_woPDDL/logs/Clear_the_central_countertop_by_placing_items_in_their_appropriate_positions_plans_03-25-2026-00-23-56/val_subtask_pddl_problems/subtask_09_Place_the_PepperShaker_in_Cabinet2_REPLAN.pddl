(define (problem place-pepperShaker-in-cabinet2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    cabinet2 - object
    floor - object
    countertop1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 pepperShaker)
    (at-location pepperShaker countertop1)
    (at-location cabinet2 floor)
    (object-close robot1 cabinet2)
  )

  (:goal (and
    (at-location pepperShaker cabinet2)
    (object-close robot1 cabinet2)
  ))

  (:metric minimize (total-cost))
)