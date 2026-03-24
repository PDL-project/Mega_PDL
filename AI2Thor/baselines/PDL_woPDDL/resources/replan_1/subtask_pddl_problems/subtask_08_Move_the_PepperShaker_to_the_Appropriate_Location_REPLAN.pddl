```pddl
(define (problem move-pepperShaker-to-cabinet2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pepperShaker - object
    cabinet2 - object
    kitchen - object
    countertop1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pepperShaker countertop1)
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