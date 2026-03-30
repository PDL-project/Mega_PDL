```lisp
(define (problem put-remotecontrol-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    remotecontrol - object
    sidetable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location remotecontrol sidetable)
    (at-location sofa floor)
  )

  (:goal (and
    (at-location remotecontrol sofa)
  ))
)
```