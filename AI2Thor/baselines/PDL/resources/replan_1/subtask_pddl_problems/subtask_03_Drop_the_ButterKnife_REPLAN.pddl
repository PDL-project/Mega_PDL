```pddl
(define (problem drop-butterknife)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    countertop1 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 butterknife)
    (at-location countertop1 kitchen)
  )

  (:goal (and
    (at-location butterknife countertop1)
    (not (holding robot1 butterknife))
  ))
)
```