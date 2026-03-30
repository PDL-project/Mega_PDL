(define (problem put-keychain-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    box - object
    sidetable1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location keychain sidetable1)
    (at-location box floor)
  )

  (:goal (and
    (at-location keychain box)
  ))

  (:metric minimize (total-cost))
)