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
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location keychain sidetable1)
    (at-location box floor)
    (object-close robot1 box)
    (not (holding robot1 keychain))
  )

  (:goal (and
    (at-location keychain box)
    (not (holding robot1 keychain))
    (object-close robot1 box)
  ))

  (:metric minimize (total-cost))
)