```pddl
(define (problem move-pillow)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pillow - object
    sofa - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pillow sofa)
    (at-location sofa floor)
    (not (holding robot1 pillow))
  )

  (:goal (and
    (at-location pillow sofa)
    (not (holding robot1 pillow))
  ))
)
```