(define (problem slice-tomato-into-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    tomato - object
    bowl - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location knife countertop)
    (at-location tomato countertop)
    (at-location bowl countertop)

    (not (holding robot1 knife))
    (not (holding robot1 tomato))
  )

  (:goal (and
    (sliced tomato)
    (at-location tomato bowl)
  ))
)