(define (problem move-apple-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    countertop - object
    countertop1 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location apple countertop)
    (at-location countertop1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location apple countertop1)
  ))

  (:metric minimize (total-cost))
)