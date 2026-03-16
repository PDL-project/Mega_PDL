```lisp
(define (problem move-pencil-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    sofa - object
    sidetable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pencil sofa)
    (at-location sidetable floor)
    (not (holding robot1 pencil))
  )

  (:goal (and
    (at-location pencil sidetable)
    (not (holding robot1 pencil))
  ))
)
```