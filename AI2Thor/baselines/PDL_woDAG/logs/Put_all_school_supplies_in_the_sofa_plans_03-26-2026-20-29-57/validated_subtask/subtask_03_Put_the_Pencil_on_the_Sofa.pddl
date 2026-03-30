(define (problem put-pencil-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    coffeetable - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pencil coffeetable)
    (at-location sofa floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location pencil sofa)
  ))

  (:metric minimize (total-cost))
)