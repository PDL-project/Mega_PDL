```pddl
(define (problem move-pepperShaker)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    cabinet2 - object
    counterTop - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pepperShaker counterTop)
    (at-location cabinet2 floor)
    (object-close robot1 cabinet2)
    (not (holding robot1 pepperShaker))
  )

  (:goal (and
    (at-location pepperShaker cabinet2)
    (object-close robot1 cabinet2)
  ))
)
```