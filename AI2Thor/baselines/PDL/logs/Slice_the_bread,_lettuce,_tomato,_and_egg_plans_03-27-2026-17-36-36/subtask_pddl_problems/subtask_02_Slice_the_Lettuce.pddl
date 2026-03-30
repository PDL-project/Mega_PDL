```pddl
(define (problem slice-lettuce)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    knife - object
    countertop - object
    drawer - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location lettuce countertop)
    (at-location knife drawer)

    (object-close robot1 drawer)
  )

  (:goal (and
    (sliced lettuce)
    (at-location lettuce countertop)
  ))
)
```