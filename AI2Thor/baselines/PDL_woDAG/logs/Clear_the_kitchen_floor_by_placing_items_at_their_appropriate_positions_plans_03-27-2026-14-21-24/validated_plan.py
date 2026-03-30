(define (problem place-apple-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    countertop1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location apple floor)
    (at-location countertop1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location apple countertop1)
  ))

  (:metric minimize (total-cost))
)