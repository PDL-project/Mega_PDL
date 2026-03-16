(define (problem move-keychain-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    sidetable - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location keychain sofa)
    (at-location sidetable floor)
    (not (holding robot1 keychain))
    (object-close robot1 sidetable)
  )

  (:goal (and
    (at-location keychain sidetable)
    (not (holding robot1 keychain))
    (object-close robot1 sidetable)
  ))

  (:metric minimize (total-cost))
)