(define (problem place-bread-in-drawer)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    bowl1 - object
    cabinet1 - object
    drawer1 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl1)
    (at-location bread floor)
    (object-close robot1 cabinet1)
    (object-open robot1 drawer1)
  )

  (:goal (and
    (at-location bread drawer1)
    (object-close robot1 drawer1)
  ))

  (:metric minimize (total-cost))
)