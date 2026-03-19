```pddl
(define (problem clean-the-cup)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cup - object
    cabinet - object
    sink - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cup cabinet)
    (at-location sink floor)

    (object-close robot1 cabinet)
    (not (holding robot1 cup))
  )

  (:goal (and
    (cleaned robot1 cup)
    (at-location cup sink)
  ))
)
```