(define (problem put-remotecontrol-on-coffeetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remotecontrol - object
    sidetable2 - object
    coffeetable - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location remotecontrol sidetable2)
    (at-location coffeetable floor)
    (not (holding robot1 remotecontrol))
  )

  (:goal (and
    (at-location remotecontrol coffeetable)
    (not (holding robot1 remotecontrol))
  ))

  (:metric minimize (total-cost))
)