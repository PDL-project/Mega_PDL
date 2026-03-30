```pddl
(define (problem put-creditcard-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    creditcard - object
    box - object
    diningtable - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location creditcard diningtable)
    (at-location box floor)
    (object-close robot1 box)
  )

  (:goal (and
    (at-location creditcard box)
    (object-close robot1 box)
  ))
)
```