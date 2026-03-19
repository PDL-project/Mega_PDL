(define (problem move-keychain-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    sofa - object
    sidetable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location keychain sofa)
    (not (holding robot1 keychain))
  )

  (:goal (and
    (at-location keychain sidetable)
    (not (holding robot1 keychain))
  ))
)