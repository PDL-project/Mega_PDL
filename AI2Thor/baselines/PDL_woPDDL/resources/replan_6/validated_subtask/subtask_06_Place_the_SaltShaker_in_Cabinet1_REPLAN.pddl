(define (problem place-saltshaker-in-cabinet1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    saltShaker - object
    cabinet1 - object
    floor - object
    kitchen - object
    countertop1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cabinet1 floor)
    (object-close robot1 cabinet1)
    (at-location saltShaker countertop1)
  )

  (:goal (and
    (at-location saltShaker cabinet1)
    (object-close robot1 cabinet1)
  ))

  (:metric minimize (total-cost))
)