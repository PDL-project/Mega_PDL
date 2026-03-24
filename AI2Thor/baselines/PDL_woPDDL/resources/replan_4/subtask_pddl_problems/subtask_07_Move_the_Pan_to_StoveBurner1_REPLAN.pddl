```pddl
(define (problem move-pan-to-stoveburner1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pan - object
    stoveburner1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pan floor)
    (not (holding robot1 pan))
  )

  (:goal (and
    (at-location pan stoveburner1)
  ))
)
```