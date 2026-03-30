(define (problem slice-lettuce)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    knife - object
    countertop - object
    drawer1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location lettuce countertop)
    (at-location knife drawer1)

    (not (holding robot1 lettuce))
    (not (holding robot1 knife))

    (object-close robot1 drawer1)
  )

  (:goal (and
    (sliced lettuce)
    (at-location lettuce countertop)
  ))

  (:metric minimize (total-cost))
)