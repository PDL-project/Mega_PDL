```pddl
(define (problem move-pillow-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pillow - object
    sofa - object
    sidetable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pillow sofa)
    (at-location sidetable floor)
    (not (holding robot1 pillow))
  )

  (:goal (and
    (at-location pillow sidetable)
  ))
)
```