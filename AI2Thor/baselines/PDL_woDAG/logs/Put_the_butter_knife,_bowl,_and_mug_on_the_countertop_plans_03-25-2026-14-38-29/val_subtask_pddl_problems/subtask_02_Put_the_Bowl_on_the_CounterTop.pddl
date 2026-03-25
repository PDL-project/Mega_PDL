(define (problem put-bowl-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location bowl floor)
    (at-location countertop floor)
    (not (holding robot1 bowl))
    (not (object-close robot1 countertop))
  )

  (:goal (and
    (at-location bowl countertop)
    (not (holding robot1 bowl))
  ))

  (:metric minimize (total-cost))
)