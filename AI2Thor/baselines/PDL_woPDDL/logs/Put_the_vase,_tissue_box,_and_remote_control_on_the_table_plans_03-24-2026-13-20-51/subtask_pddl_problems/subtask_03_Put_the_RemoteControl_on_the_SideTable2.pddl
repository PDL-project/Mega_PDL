```pddl
(define (problem put-remote-on-sidetable2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remoteControl - object
    sideTable2 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location remoteControl sideTable2)
    (at-location sideTable2 floor)
    (not (holding robot1 remoteControl))
  )

  (:goal (and
    (at-location remoteControl sideTable2)
    (not (holding robot1 remoteControl))
  ))
)
```