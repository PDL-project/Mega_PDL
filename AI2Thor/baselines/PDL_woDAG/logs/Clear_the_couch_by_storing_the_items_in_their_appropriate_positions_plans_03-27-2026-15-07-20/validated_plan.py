(define (problem store-keychain-on-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    sidetable1 - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location keychain sofa)
    (at-location sidetable1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location keychain sidetable1)
  ))

  (:metric minimize (total-cost))
)