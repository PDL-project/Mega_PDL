```pddl
(define (problem close-curtains)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    curtains - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location curtains floor)
    (object-open robot1 curtains)
  )

  (:goal (and
    (object-close robot1 curtains)
  ))
)
```