```pddl
(define (problem put-butterknife-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    drawer2 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (at-location butterknife countertop)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
    (not (holding robot1 butterknife))
  )

  (:goal (and
    (at-location butterknife drawer2)
    (object-close robot1 drawer2)
  ))
)
```