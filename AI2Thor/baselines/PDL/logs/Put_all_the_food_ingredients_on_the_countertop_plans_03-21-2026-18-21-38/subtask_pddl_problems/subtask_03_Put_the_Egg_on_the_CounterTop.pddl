```pddl
(define (problem put-egg-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    egg - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location egg countertop)
    (at-location countertop floor)
    (not (holding robot1 egg))
  )

  (:goal (and
    (at-location egg countertop)
    (not (holding robot1 egg))
  ))
)
```