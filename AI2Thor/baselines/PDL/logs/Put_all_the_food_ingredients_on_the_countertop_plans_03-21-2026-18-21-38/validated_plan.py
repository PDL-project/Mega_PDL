(define (problem put-apple-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    fridge - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (at-location apple fridge)
    (at-location fridge floor)
    (at-location countertop floor)

    (is-fridge fridge)
    (not (holding robot1 apple))
    (fridge-open fridge)
  )

  (:goal (and
    (at-location apple countertop)
    (not (holding robot1 apple))
    (not (fridge-open fridge))
  ))
)