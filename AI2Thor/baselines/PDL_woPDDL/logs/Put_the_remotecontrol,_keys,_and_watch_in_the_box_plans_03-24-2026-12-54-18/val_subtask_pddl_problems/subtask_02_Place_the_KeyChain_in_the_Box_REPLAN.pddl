(define (problem place-keychain-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    box1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 box1)
    (holding robot1 keychain)
    (object-close robot1 box1)
  )

  (:goal (and
    (at-location keychain box1)
    (object-close robot1 box1)
  ))

  (:metric minimize (total-cost))
)