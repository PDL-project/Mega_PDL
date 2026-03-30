```pddl
(define (problem move-pencil-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    diningtable - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pencil diningtable)
    (at-location sofa floor)
  )

  (:goal (and
    (at-location pencil sofa)
  ))
)
```