```pddl
(define (problem store-pencil)
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
    (at-location sidetable3 floor)
  )

  (:goal (and
    (at-location pencil sidetable3)
  ))
)
```