(define (problem put-remotecontrol-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remotecontrol - object
    sidetable - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location remotecontrol sidetable)
    (at-location sofa floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location remotecontrol sofa)
  ))

  (:metric minimize (total-cost))
)