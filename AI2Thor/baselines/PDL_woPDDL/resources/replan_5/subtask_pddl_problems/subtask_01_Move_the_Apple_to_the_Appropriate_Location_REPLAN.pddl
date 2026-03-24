```pddl
(define (problem move-apple-to-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    bowl1 - object
    kitchen - object
    countertop1 - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location apple countertop1)
    (not (holding robot1 apple))
  )

  (:goal (and
    (at-location apple bowl1)
    (not (holding robot1 apple))
  ))
)
```