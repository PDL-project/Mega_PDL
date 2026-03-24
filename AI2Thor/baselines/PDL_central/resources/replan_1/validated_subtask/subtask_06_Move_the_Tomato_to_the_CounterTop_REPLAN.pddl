(define (problem move-tomato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    countertop1 - object
    drawer1 - object
    kitchen - object
    bowl1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl1)
    (at-location tomato kitchen)
    (at-location countertop1 kitchen)
    (object-close robot1 drawer1)
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location tomato countertop1)
  ))

  (:metric minimize (total-cost))
)