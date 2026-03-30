(define (problem place-sliced-vegetables-on-plate)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    plate - object
    lettuce - object
    tomato - object
    countertop - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location plate countertop)
    (at-location lettuce countertop)
    (at-location tomato countertop)

    (not (holding robot1 plate))
    (not (holding robot1 lettuce))
    (not (holding robot1 tomato))

    ;; Ensure receptacles are open if needed
    (not (object-close robot1 countertop))
  )

  (:goal (and
    (at-location lettuce plate)
    (at-location tomato plate)
  ))

  (:metric minimize (total-cost))
)