```pddl
(define (problem place-bread-in-cabinet1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    cabinet1 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 bread)
    (at-location cabinet1 floor)
    (object-close robot1 cabinet1)
  )

  (:goal (and
    (at-location bread cabinet1)
    (object-close robot1 cabinet1)
  ))
)
```