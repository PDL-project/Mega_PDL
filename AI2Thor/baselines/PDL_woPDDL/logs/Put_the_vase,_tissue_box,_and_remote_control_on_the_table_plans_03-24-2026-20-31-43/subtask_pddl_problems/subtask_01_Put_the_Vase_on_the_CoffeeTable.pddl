```pddl
(define (problem put-vase-on-coffeetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    vase - object
    sideTable1 - object
    coffeeTable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location vase sideTable1)
    (at-location coffeeTable floor)
    (not (holding robot1 vase))
  )

  (:goal (and
    (at-location vase coffeeTable)
    (not (holding robot1 vase))
  ))
)
```