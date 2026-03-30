```pddl
(define (problem slice-lettuce)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    knife - object
    countertop - object
    drawer1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location lettuce countertop)
    (at-location knife drawer1)

    (object-close robot1 drawer1)
  )

  (:goal (and
    (sliced lettuce)
  ))
)
```