(define (problem place-keychain-on-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    sidetable - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 sidetable)
    (holding robot1 keychain)
  )

  (:goal (and
    (at-location keychain sidetable)
    (not (holding robot1 keychain))
  ))

  (:metric minimize (total-cost))
)