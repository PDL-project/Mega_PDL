(define (problem put-newspaper-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    newspaper - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location newspaper diningtable)
    (not (holding robot1 newspaper))
  )

  (:goal (and
    (at-location newspaper sofa)
    (not (holding robot1 newspaper))
  ))

  (:metric minimize (total-cost))
)