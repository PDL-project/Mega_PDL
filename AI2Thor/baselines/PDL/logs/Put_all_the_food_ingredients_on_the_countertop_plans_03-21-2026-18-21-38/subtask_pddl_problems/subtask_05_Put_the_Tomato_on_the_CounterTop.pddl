```pddl
(define (problem put-tomato-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location tomato floor)
    (at-location countertop floor)
    (not (holding robot1 tomato))
  )

  (:goal (and
    (at-location tomato countertop)
    (not (holding robot1 tomato))
  ))
)
```