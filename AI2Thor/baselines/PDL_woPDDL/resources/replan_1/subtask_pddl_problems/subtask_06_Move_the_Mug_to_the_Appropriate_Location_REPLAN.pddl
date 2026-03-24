```pddl
(define (problem move-mug-to-cabinet1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    cabinet1 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 lettuce)
    (at-location cabinet1 floor)
    (object-close robot1 cabinet1)
  )

  (:goal (and
    (at-location mug cabinet1)
    (object-close robot1 cabinet1)
  ))
)
```