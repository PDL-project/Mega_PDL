```pddl
(define (problem move-saltshaker-to-cabinet3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    saltShaker - object
    cabinet3 - object
    countertop1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)

    (at-location saltShaker countertop1)
    (at-location cabinet3 floor)

    (object-close robot1 cabinet3)
    (not (holding robot1 saltShaker))
  )

  (:goal (and
    (at-location saltShaker cabinet3)
    (not (holding robot1 saltShaker))
    (object-close robot1 cabinet3)
  ))
)
```