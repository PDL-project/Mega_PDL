```pddl
(define (problem store-spatula)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spatula - object
    drawer2 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 spatula)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location spatula drawer2)
    (object-close robot1 drawer2)
  ))
)
```