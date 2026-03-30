```pddl
(define (problem store-pencil-on-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    sofa - object
    sidetable3 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pencil sofa)
  )

  (:goal (and
    (at-location pencil sidetable3)
  ))
)
```