```pddl
(define (problem move-saltshaker)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    saltshaker - object
    cabinet3 - object
    countertop - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location saltshaker countertop)
    (at-location cabinet3 floor)
    (object-close robot1 cabinet3)
    (not (holding robot1 saltshaker))
  )

  (:goal (and
    (at-location saltshaker cabinet3)
    (object-close robot1 cabinet3)
  ))
)
```