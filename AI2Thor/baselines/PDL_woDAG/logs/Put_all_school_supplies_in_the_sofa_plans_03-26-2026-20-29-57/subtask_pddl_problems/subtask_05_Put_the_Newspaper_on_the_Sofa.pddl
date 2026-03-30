```pddl
(define (problem put-newspaper-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    newspaper - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location newspaper diningtable)
    (at-location sofa floor)
  )

  (:goal (and
    (at-location newspaper sofa)
  ))
)
```