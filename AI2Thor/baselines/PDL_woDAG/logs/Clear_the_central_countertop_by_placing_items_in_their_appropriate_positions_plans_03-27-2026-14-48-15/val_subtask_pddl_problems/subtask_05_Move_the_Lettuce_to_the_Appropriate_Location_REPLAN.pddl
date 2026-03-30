(define (problem place-apple-and-move-lettuce)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    lettuce - object
    bowl1 - object
    cabinet1 - object
    countertop3 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 apple)
    (at-location lettuce countertop3)
    (object-close robot1 cabinet1)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location apple bowl1)
    (at-location lettuce cabinet1)
    (object-close robot1 cabinet1)
  ))

  (:metric minimize (total-cost))
)