(define (problem slice-tomato)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    knife - object
    countertop - object
    drawer1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location tomato countertop)
    (at-location knife drawer1)

    (object-close robot1 drawer1)
    (= (total-cost) 0)
  )

  (:goal (and
    (sliced tomato)
  ))

  (:metric minimize (total-cost))
)