(define (problem move-apple-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
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
    (at-location apple kitchen)
    (object-close robot1 drawer1)
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location apple countertop1)
  ))

  (:metric minimize (total-cost))
)