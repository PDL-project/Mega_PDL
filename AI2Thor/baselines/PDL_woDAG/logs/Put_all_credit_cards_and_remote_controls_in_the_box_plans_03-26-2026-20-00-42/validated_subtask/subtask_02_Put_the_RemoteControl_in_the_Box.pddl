(define (problem put-remotecontrol-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remotecontrol - object
    box - object
    sidetable1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location remotecontrol sidetable1)
    (at-location box floor)
  )

  (:goal (and
    (at-location remotecontrol box)
  ))

  (:metric minimize (total-cost))
)