```pddl
(define (problem slice-egg)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    egg - object
    butterknife - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location egg countertop)
    (at-location butterknife countertop)

    (not (holding robot1 egg))
    (not (holding robot1 butterknife))
  )

  (:goal (and
    (sliced egg)
    (at-location egg countertop)
  ))
)
```