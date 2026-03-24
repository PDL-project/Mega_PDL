```pddl
(define (problem slice-lettuce)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    butterknife - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location lettuce countertop)
    (at-location butterknife countertop)

    (not (holding robot1 lettuce))
    (not (holding robot1 butterknife))
  )

  (:goal (and
    (sliced lettuce)
    (at-location lettuce countertop)
  ))
)
```