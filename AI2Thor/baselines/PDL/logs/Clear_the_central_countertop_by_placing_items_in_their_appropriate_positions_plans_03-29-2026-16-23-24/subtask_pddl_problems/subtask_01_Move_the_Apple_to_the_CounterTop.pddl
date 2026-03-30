```pddl
(define (problem move-apple-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    countertop - object
    countertop2 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 countertop)
    (hand-empty robot1)
    (at-location apple countertop)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location apple countertop2)
  ))
)
```