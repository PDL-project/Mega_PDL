(define (problem place-apple-in-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    bowl1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 apple)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location apple bowl1)
  ))

  (:metric minimize (total-cost))
)