```pddl
(define (problem place-pen-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    drawer2 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 pen)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location pen drawer2)
    (object-close robot1 drawer2)
  ))
)
```