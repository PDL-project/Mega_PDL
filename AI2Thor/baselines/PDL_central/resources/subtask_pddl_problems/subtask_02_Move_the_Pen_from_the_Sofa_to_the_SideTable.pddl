```pddl
(define (problem move-pen-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    sofa - object
    sidetable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pen sofa)
    (at-location sidetable floor)
    (not (holding robot1 pen))
  )

  (:goal (and
    (at-location pen sidetable)
    (not (holding robot1 pen))
  ))
)
```