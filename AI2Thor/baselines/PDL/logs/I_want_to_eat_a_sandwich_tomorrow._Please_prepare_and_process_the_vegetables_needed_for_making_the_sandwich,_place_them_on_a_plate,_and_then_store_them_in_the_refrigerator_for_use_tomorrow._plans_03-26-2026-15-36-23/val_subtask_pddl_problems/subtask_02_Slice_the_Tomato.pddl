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
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location knife countertop)
    (at-location tomato countertop)

    (not (holding robot1 knife))
    (not (holding robot1 tomato))

    ;; Ensure the robot is not at any other object initially
    (not (at robot1 tomato))
    (not (at robot1 countertop))
  )

  (:goal (and
    (sliced tomato)
  ))

  (:metric minimize (total-cost))
)