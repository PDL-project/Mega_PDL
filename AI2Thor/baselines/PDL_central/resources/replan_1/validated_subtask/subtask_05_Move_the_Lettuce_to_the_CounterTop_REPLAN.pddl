(define (problem move-lettuce-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    countertop1 - object
    kitchen - object
    bowl1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl1)
    (at-location lettuce kitchen)
    (at-location countertop1 kitchen)
    (not (object-close robot1 bowl1))
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location lettuce countertop1)
  ))

  (:metric minimize (total-cost))
)