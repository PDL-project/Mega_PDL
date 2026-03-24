(define (problem place-potato-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location potato floor)
    (not (holding robot1 potato))
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location potato countertop1)
  ))

  (:metric minimize (total-cost))
)