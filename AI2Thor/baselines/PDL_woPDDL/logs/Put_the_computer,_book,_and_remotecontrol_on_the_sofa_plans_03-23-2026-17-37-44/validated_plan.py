(define (problem put-laptop-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    laptop - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location laptop diningtable)
    (at-location sofa floor)
    (not (holding robot1 laptop))
  )

  (:goal (and
    (at-location laptop sofa)
    (not (holding robot1 laptop))
  ))
)