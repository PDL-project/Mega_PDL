(define (problem slice-apple)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    knife - object
    fridge - object
    countertop - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location apple fridge)
    (at-location knife countertop)

    (is-fridge fridge)
    (fridge-open fridge)

    (not (holding robot1 apple))
    (not (holding robot1 knife))
  )

  (:goal (and
    (sliced apple)
    (at-location apple countertop)
  ))

  (:metric minimize (total-cost))
)