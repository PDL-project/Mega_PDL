```pddl
(define (problem move-pepperShaker)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    cabinet5 - object
    counterTop - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pepperShaker counterTop)
    (at-location cabinet5 floor)
    (object-close robot1 cabinet5)
  )

  (:goal (and
    (at-location pepperShaker cabinet5)
    (object-close robot1 cabinet5)
  ))
)
```