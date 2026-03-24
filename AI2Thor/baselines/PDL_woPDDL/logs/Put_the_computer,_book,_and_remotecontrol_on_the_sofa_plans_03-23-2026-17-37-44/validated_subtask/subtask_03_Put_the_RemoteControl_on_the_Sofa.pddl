(define (problem put-remotecontrol-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remotecontrol - object
    sidetable1 - object
    sofa - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location remotecontrol sidetable1)
    (at-location sofa floor)
    (not (holding robot1 remotecontrol))
  )

  (:goal (and
    (at-location remotecontrol sofa)
    (not (holding robot1 remotecontrol))
  ))

  (:metric minimize (total-cost))
)