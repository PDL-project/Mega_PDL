(define (problem place-bread-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location bread floor)
    (not (holding robot1 bread))
    (not (object-close robot1 countertop1))
  )

  (:goal (and
    (at-location bread countertop1)
  ))

  (:metric minimize (total-cost))
)