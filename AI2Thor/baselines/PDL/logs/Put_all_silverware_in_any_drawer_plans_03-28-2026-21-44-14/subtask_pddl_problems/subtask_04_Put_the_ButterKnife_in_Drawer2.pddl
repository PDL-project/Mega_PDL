```pddl
(define (problem put-butterknife-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterKnife - object
    drawer2 - object
    counterTop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location butterKnife counterTop)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location butterKnife drawer2)
    (object-close robot1 drawer2)
  ))
)
```