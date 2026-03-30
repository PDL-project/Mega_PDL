```pddl
(define (problem move-butterknife-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    countertop - object
    countertop2 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location butterknife countertop)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location butterknife countertop2)
  ))
)
```