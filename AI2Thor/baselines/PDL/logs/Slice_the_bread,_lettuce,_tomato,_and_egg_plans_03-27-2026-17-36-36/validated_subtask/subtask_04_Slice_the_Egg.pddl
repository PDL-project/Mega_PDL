(define (problem slice-egg)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    egg - object
    knife - object
    countertop - object
    drawer1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location egg countertop)
    (at-location knife drawer1)

    (object-close robot1 drawer1)
    (= (total-cost) 0)
  )

  (:goal (and
    (sliced egg)
  ))

  (:metric minimize (total-cost))
)