(define (problem move-fork-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    countertop - object
    countertop3 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location fork countertop)
    (at-location countertop3 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location fork countertop3)
  ))

  (:metric minimize (total-cost))
)