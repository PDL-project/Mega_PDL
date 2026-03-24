(define (problem drop-bowl-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bowl1 - object
    countertop1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl1)
    (at-location countertop1 kitchen)
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location bowl1 countertop1)
    (not (holding robot1 bowl1))
  ))

  (:metric minimize (total-cost))
)