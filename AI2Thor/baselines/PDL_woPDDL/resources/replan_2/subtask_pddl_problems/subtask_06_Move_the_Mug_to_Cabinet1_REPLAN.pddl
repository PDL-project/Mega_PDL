```pddl
(define (problem move-mug-to-cabinet1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    cabinet1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location mug floor)
    (at-location cabinet1 floor)
    (object-close robot1 cabinet1)
  )

  (:goal (and
    (at-location mug cabinet1)
    (object-close robot1 cabinet1)
  ))
)
```