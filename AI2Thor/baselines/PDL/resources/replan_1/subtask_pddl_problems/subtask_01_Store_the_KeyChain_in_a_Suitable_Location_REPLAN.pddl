```pddl
(define (problem store-keychain)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    armchair1 - object
    sidetable - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 sidetable)
    (holding robot1 keychain)
  )

  (:goal (and
    (at-location keychain armchair1)
  ))
)
```