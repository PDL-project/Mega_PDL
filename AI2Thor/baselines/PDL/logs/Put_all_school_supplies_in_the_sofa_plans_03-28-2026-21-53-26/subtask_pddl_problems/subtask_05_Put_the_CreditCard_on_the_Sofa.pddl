```pddl
(define (problem put-creditcard-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    creditcard - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location creditcard diningtable)
    (at-location sofa floor)
  )

  (:goal (and
    (at-location creditcard sofa)
  ))
)
```