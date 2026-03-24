```pddl
(define (problem move-lettuce-to-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    lettuce - object
    bowl1 - object
    floor - object
    cabinet1 - object
    butterknife - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location lettuce floor)
    (at-location butterknife floor)
    (at-location cabinet1 floor)

    (holding robot1 butterknife)
    (object-close robot1 cabinet1)
  )

  (:goal (and
    (at-location lettuce bowl1)
    (not (holding robot1 lettuce))
  ))
)
```