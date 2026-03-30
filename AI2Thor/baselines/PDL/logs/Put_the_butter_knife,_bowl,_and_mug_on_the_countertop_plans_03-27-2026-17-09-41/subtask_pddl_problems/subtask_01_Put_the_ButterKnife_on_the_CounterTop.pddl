```pddl
(define (problem put-butterknife-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterKnife - object
    counterTop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location butterKnife floor)
    (at-location counterTop floor)
  )

  (:goal (and
    (at-location butterKnife counterTop)
  ))
)
```