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
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location egg countertop)
    (at-location knife drawer1)

    (not (holding robot1 egg))
    (not (holding robot1 knife))

    (object-close robot1 drawer1)
  )

  (:goal (and
    (sliced egg)
  ))

  (:metric minimize (total-cost))
)