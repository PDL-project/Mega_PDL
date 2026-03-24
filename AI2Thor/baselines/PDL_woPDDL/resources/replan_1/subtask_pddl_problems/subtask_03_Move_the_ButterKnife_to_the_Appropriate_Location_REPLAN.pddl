```pddl
(define (problem move-butterknife-to-drawer1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    drawer1 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location butterknife floor)
    (at-location drawer1 floor)
    (object-close robot1 drawer1)
    (not (holding robot1 butterknife))
  )

  (:goal (and
    (at-location butterknife drawer1)
    (object-close robot1 drawer1)
  ))
)
```