```pddl
(define (problem move-apple-to-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    bowl - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location apple countertop)
    (at-location bowl floor)
  )

  (:goal (and
    (at-location apple bowl)
  ))
)
```