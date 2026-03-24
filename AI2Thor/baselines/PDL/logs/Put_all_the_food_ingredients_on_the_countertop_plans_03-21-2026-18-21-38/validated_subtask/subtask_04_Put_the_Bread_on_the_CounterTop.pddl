(define (problem put-bread-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    countertop - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location bread floor)
    (at-location countertop floor)

    (not (holding robot1 bread))
  )

  (:goal (and
    (at-location bread countertop)
    (not (holding robot1 bread))
  ))

  (:metric minimize (total-cost))
)