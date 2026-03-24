```pddl
(define (problem put-remote-on-coffee-table)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remoteControl - object
    coffeeTable - object
    sideTable2 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location remoteControl sideTable2)
    (at-location coffeeTable floor)
    (not (holding robot1 remoteControl))
  )

  (:goal (and
    (at-location remoteControl coffeeTable)
    (not (holding robot1 remoteControl))
  ))
)
```