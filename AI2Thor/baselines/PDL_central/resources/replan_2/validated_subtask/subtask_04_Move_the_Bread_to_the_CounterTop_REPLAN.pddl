(define (problem move-bread-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    bowl - object
    cabinet1 - object
    countertop1 - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl)
    (at-location bread floor)
    (object-close robot1 cabinet1)
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location bread countertop1)
  ))

  (:metric minimize (total-cost))
)