(define (problem move-fork-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    countertop - object
    countertop2 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location fork countertop)
    (at-location countertop2 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location fork countertop2)
  ))

  (:metric minimize (total-cost))
)