(define (problem slice-tomato-onto-plate)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    tomato - object
    plate - object
    countertop - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 countertop)

    (at-location knife countertop)
    (at-location tomato countertop)
    (at-location plate countertop)

    (not (holding robot1 knife))
    (not (holding robot1 tomato))
  )

  (:goal (and
    (sliced tomato)
    (at-location tomato plate)
  ))

  (:metric minimize (total-cost))
)