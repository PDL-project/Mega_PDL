```pddl
(define (problem slice-tomato)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    butterknife - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location tomato countertop)
    (at-location butterknife countertop)

    (not (holding robot1 tomato))
    (not (holding robot1 butterknife))
  )

  (:goal (and
    (sliced tomato)
  ))
)
```