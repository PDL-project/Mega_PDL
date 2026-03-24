```pddl
(define (problem move-tomato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    countertop1 - object
    drawer1 - object
    kitchen - object
    bowl1 - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bowl1)
    (at-location tomato kitchen)
    (at-location countertop1 kitchen)
    (object-close robot1 drawer1)
  )

  (:goal (and
    (at-location tomato countertop1)
  ))
)
```