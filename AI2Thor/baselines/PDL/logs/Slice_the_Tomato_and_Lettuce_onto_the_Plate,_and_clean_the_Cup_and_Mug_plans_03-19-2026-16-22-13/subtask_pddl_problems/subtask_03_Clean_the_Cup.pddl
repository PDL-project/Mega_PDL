```pddl
(define (problem clean-the-cup)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cup - object
    sink - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cup floor)
    (at-location sink floor)
    (not (holding robot1 cup))
  )

  (:goal (and
    (cleaned robot1 cup)
  ))
)
```