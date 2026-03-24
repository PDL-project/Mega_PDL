(define (problem place-bowl-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    countertop1 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (holding robot1 bowl)
    (at-location countertop1 floor)
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location bowl countertop1)
    (not (holding robot1 bowl))
  ))

  (:metric minimize (total-cost))
)