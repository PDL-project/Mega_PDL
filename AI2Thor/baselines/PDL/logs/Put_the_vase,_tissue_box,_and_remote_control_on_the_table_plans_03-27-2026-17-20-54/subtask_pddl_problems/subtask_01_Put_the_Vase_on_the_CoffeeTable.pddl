```pddl
(define (problem put-vase-on-coffeetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    vase - object
    sidetable1 - object
    coffeetable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location vase sidetable1)
    (at-location coffeetable floor)
  )

  (:goal (and
    (at-location vase coffeetable)
  ))
)
```