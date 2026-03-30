```pddl
(define (problem move-saltshaker)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    saltshaker - object
    cabinet6 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location saltshaker countertop)
    (at-location cabinet6 floor)
    (object-close robot1 cabinet6)
  )

  (:goal (and
    (at-location saltshaker cabinet6)
    (object-close robot1 cabinet6)
  ))
)
```