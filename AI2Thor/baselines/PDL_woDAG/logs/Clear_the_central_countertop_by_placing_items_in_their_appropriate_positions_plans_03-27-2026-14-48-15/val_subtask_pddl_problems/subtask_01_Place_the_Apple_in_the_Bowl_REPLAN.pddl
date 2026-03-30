(define (problem place-apple-in-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    bowl1 - object
    floor - object
    robot3 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (holding robot1 apple)
    (at-location apple robot3)
    (at-location bowl1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location apple bowl1)
  ))

  (:metric minimize (total-cost))
)