(define (problem move-pepperShaker-to-cabinet2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    cabinet2 - object
    countertop1 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 soapBottle) ;; Robot starts at soapBottle location
    (at-location pepperShaker countertop1)
    (at-location cabinet2 floor)
    (not (holding robot1 pepperShaker))
    (object-close robot1 cabinet2) ;; Cabinet2 is initially closed
  )

  (:goal (and
    (at-location pepperShaker cabinet2)
    (not (holding robot1 pepperShaker))
    (object-close robot1 cabinet2)
  ))

  (:metric minimize (total-cost))
)