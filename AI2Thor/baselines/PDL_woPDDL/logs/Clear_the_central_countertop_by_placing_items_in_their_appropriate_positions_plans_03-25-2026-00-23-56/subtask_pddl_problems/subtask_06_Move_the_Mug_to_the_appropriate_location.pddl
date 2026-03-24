```pddl
(define (problem move-mug-to-cabinet)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    mug - object
    cabinet1 - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location mug countertop)
    (at-location cabinet1 floor)
    (not (holding robot1 mug))
    (object-close robot1 cabinet1)
  )

  (:goal (and
    (at-location mug cabinet1)
    (object-close robot1 cabinet1)
  ))
)
```