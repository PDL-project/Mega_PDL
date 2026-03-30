```pddl
(define (problem move-mug-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    countertop - object
    countertop2 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 countertop)
    (hand-empty robot1)
    (at-location mug countertop)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location mug countertop2)
  ))
)
```