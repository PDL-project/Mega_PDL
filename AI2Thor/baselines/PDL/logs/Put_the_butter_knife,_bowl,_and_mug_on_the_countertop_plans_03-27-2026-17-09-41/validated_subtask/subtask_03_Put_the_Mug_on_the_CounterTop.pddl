(define (problem put-mug-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location mug floor)
    (at-location countertop floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location mug countertop)
  ))

  (:metric minimize (total-cost))
)