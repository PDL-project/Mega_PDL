```pddl
(define (problem move-lettuce-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    countertop1 - object
    butterknife - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 butterknife)
    (at-location lettuce floor)
    (at-location countertop1 kitchen)
  )

  (:goal (and
    (at-location lettuce countertop1)
  ))
)
```