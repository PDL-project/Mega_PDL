(define (problem store-keychain-in-box1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    box1 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 keychain)
    (at-location box1 floor)
    (object-close robot1 box1)
  )

  (:goal (and
    (at-location keychain box1)
    (not (holding robot1 keychain))
    (object-close robot1 box1)
  ))

  (:metric minimize (total-cost))
)