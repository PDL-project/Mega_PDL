(define (problem put-pencil-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    coffeetable - object
    sofa - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pencil coffeetable)
    (at-location sofa floor)
    (not (holding robot1 pencil))
  )

  (:goal (and
    (at-location pencil sofa)
    (not (holding robot1 pencil))
  ))

  (:metric minimize (total-cost))
)