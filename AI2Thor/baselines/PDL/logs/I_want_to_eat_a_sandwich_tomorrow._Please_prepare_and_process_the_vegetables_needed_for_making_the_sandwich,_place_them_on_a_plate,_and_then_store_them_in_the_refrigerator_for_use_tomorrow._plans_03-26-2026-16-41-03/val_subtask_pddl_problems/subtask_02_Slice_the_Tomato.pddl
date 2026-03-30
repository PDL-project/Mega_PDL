(define (problem slice-tomato)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    tomato - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location knife countertop)
    (at-location tomato countertop)

    (not (holding robot1 knife))
    (not (holding robot1 tomato))
    (= (total-cost) 0)
  )

  (:goal (and
    (sliced tomato)
    (at-location tomato countertop)
  ))

  (:metric minimize (total-cost))
)