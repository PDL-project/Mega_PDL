```pddl
(define (problem move-pencil-to-armchair2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    sofa1 - object
    armchair2 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pencil sofa1)
    (not (holding robot1 pencil))
  )

  (:goal (and
    (at-location pencil armchair2)
  ))
)
```