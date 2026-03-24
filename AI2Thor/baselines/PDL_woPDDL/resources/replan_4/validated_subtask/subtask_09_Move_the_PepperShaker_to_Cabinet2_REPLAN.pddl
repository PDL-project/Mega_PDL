(define (problem move-pepperShaker-to-cabinet2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    cabinet2 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pepperShaker floor)
    (at-location cabinet2 floor)
    (object-close robot1 cabinet2)
    (holding robot1 apple)
  )

  (:goal (and
    (at-location pepperShaker cabinet2)
    (object-close robot1 cabinet2)
  ))

  (:metric minimize (total-cost))
)