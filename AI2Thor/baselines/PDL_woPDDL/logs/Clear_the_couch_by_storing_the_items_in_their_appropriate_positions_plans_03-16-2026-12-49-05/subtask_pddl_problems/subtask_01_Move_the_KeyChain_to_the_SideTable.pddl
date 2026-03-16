```pddl
(define (problem move-keychain-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    sidetable - object
    sofa - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location keychain sofa)
    (at-location sidetable floor)
    (not (holding robot1 keychain))
  )

  (:goal (and
    (at-location keychain sidetable)
    (not (holding robot1 keychain))
  ))
)
```