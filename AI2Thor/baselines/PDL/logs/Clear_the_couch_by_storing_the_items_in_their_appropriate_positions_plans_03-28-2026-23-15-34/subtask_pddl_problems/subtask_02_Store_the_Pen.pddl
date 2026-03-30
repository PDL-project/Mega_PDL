```pddl
(define (problem store-the-pen)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    sofa - object
    sidetable2 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pen sofa)
    (at-location sidetable2 floor)
  )

  (:goal (and
    (at-location pen sidetable2)
  ))
)
```