(define (problem put-remotecontrol-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remotecontrol - object
    box - object
    sidetable - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location remotecontrol sidetable)
    (at-location box floor)
    (object-close robot1 box)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location remotecontrol box)
    (object-close robot1 box)
  ))

  (:metric minimize (total-cost))
)