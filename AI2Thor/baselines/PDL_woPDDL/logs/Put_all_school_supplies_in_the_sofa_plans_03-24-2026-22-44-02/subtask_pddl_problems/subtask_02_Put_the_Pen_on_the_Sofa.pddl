```pddl
(define (problem put-pen-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pen diningtable)
    (at-location sofa floor)
    (not (holding robot1 pen))
  )

  (:goal (and
    (at-location pen sofa)
    (not (holding robot1 pen))
  ))
)
```