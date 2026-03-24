```pddl
(define (problem move-pencil-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pencil diningtable)
    (at-location sofa floor)
    (not (holding robot1 pencil))
  )

  (:goal (and
    (at-location pencil sofa)
  ))
)
```