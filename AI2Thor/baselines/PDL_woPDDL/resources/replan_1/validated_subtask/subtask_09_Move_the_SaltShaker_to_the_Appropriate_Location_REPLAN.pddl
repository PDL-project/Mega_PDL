(define (problem move-saltshaker-to-cabinet3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    saltshaker - object
    cabinet3 - object
    kitchen - object
    countertop1 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location saltshaker countertop1)
    (at-location cabinet3 floor)
    (object-close robot1 cabinet3)
    (not (holding robot1 saltshaker))
  )

  (:goal (and
    (at-location saltshaker cabinet3)
    (object-close robot1 cabinet3)
  ))

  (:metric minimize (total-cost))
)