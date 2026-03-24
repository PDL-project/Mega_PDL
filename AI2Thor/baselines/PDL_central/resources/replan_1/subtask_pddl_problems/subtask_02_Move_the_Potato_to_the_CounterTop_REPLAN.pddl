```pddl
(define (problem move-potato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    potato - object
    countertop1 - object
    kitchen - object
    cabinet1 - object
    bowl - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl)
    (at-location potato kitchen)
    (at-location cabinet1 kitchen)
    (object-close robot1 cabinet1)
  )

  (:goal (and
    (at-location potato countertop1)
  ))
)
```