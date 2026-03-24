```pddl
(define (problem move-book-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    book - object
    diningtable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location book diningtable)
    (not (holding robot1 book))
  )

  (:goal (and
    (at-location book sofa)
    (not (holding robot1 book))
  ))
)
```