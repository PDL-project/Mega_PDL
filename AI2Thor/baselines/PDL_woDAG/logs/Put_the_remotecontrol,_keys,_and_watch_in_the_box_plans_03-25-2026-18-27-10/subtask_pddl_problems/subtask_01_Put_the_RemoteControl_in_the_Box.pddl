```pddl
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
    (at-location remotecontrol sidetable1)
    (at-location box floor)
    (object-close robot1 box)
    (not (holding robot1 remotecontrol))
  )

  (:goal (and
    (at-location remotecontrol box)
    (object-close robot1 box)
  ))
)
```