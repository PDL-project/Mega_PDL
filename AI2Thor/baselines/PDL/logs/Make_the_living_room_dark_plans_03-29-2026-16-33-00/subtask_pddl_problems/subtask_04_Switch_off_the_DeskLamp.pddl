```pddl
(define (problem switch-off-desklamp)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    desklamp - object
    sidetable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location desklamp sidetable)
    (switch-on robot1 desklamp)
  )

  (:goal (and
    (switch-off robot1 desklamp)
  ))
)
```