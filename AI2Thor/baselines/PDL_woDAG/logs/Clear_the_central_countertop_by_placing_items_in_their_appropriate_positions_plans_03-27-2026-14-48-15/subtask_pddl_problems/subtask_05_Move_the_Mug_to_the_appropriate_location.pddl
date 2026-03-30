```pddl
(define (problem move-mug-to-cabinet3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    cabinet3 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location mug countertop)
    (at-location cabinet3 floor)
    (object-close robot1 cabinet3)
  )

  (:goal (and
    (at-location mug cabinet3)
    (object-close robot1 cabinet3)
  ))
)
```