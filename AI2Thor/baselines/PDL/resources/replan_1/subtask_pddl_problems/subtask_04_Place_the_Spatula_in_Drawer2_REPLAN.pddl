```pddl
(define (problem place-spatula-in-drawer)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    drawer2 - object
    drawer3 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 spatula)
    (at-location drawer2 floor)
    (at-location drawer3 floor)
    (object-close robot1 drawer3)
  )

  (:goal (and
    (at-location spatula drawer3)
    (object-close robot1 drawer3)
  ))
)
```