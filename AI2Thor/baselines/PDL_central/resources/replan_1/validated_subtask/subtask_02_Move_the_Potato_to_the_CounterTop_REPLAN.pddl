(define (problem move-potato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    countertop1 - object
    kitchen - object
    cabinet1 - object
    bowl - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl)
    (at-location potato kitchen)
    (at-location cabinet1 kitchen)
    (object-close robot1 cabinet1)
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location potato countertop1)
  ))

  (:metric minimize (total-cost))
)