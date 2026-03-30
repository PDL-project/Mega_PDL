(define (problem put-remotecontrol-on-coffeetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remotecontrol - object
    sidetable2 - object
    coffeetable - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location remotecontrol sidetable2)
    (at-location coffeetable floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location remotecontrol coffeetable)
  ))

  (:metric minimize (total-cost))
)