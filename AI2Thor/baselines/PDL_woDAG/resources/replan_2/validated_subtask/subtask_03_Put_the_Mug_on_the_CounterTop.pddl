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
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location mug floor)
    (at-location countertop floor)
    (not (holding robot1 mug))
  )

  (:goal (and
    (at-location mug countertop)
    (not (holding robot1 mug))
  ))

  (:metric minimize (total-cost))
)