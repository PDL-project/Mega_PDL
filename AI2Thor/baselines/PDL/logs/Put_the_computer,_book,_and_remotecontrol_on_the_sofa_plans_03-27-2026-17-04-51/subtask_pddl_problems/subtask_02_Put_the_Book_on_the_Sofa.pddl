```pddl
(define (problem put-book-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    book - object
    chair - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location book chair)
    (at-location sofa floor)
  )

  (:goal (and
    (at-location book sofa)
  ))
)
```