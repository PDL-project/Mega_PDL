(define (problem move-mug-to-cabinet1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    cabinet1 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location mug floor)
    (at-location cabinet1 floor)
    (not (object-open robot1 cabinet1))
    (not (holding robot1 mug))
  )

  (:goal (and
    (at-location mug cabinet1)
    (object-close robot1 cabinet1)
  ))

  (:metric minimize (total-cost))
)