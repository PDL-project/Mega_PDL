```pddl
(define (problem put-keychain-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    box - object
    sidetable - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location keychain sidetable)
    (at-location box floor)
    (object-close robot1 box)
    (not (holding robot1 keychain))
  )

  (:goal (and
    (at-location keychain box)
    (not (holding robot1 keychain))
    (object-close robot1 box)
  ))
)
```