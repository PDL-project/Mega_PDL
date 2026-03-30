```pddl
(define (problem put-pen-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    chair - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location pen chair)
    (at-location sofa floor)
  )

  (:goal (and
    (at-location pen sofa)
  ))
)
```