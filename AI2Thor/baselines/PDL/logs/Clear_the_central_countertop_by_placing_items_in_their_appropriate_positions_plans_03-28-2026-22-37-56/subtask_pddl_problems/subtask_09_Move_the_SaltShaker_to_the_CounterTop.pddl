```pddl
(define (problem move-saltshaker-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    saltshaker - object
    countertop - object
    countertop2 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location saltshaker countertop)
  )

  (:goal (and
    (at-location saltshaker countertop2)
  ))
)
```