(define (problem slice-apple)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    knife - object
    fridge1 - object
    countertop1 - object
    cuttingboard - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location apple fridge1)
    (at-location knife countertop1)

    (is-fridge fridge1)
    (not (fridge-open fridge1))
    (not (holding robot1 apple))
    (not (holding robot1 knife))
    (object-close robot1 fridge1)
  )

  (:goal (and
    (sliced apple)
  ))

  (:metric minimize (total-cost))
)