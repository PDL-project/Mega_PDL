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
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location bread countertop)
    (at-location knife drawer1)

    (object-close robot1 drawer1)
    (= (total-cost) 0)
  )

  (:goal (and
    (sliced bread)
  ))

  (:metric minimize (total-cost))
)