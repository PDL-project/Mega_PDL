(define (problem slice-bread)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    knife - object
    countertop - object
    drawer1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location bread countertop)
    (at-location knife drawer1)

    (not (holding robot1 bread))
    (not (holding robot1 knife))

    (object-close robot1 drawer1)
  )

  (:goal (and
    (sliced bread)
    (at-location bread countertop)
  ))

  (:metric minimize (total-cost))
)