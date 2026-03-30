```pddl
(define (problem put-watch-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    watch - object
    box - object
    sidetable1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location watch sidetable1)
    (at-location box floor)
    (object-close robot1 box)
    (not (holding robot1 watch))
  )

  (:goal (and
    (at-location watch box)
    (not (holding robot1 watch))
    (object-close robot1 box)
  ))
)
```