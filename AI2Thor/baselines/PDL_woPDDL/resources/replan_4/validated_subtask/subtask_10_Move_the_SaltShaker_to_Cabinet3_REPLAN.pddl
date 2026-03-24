(define (problem move-saltshaker-to-cabinet3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    saltShaker - object
    cabinet3 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location saltShaker floor)
    (at-location cabinet3 floor)
    (not (object-open robot1 cabinet3))
    (not (holding robot1 saltShaker))
  )

  (:goal (and
    (at-location saltShaker cabinet3)
    (object-close robot1 cabinet3)
  ))

  (:metric minimize (total-cost))
)