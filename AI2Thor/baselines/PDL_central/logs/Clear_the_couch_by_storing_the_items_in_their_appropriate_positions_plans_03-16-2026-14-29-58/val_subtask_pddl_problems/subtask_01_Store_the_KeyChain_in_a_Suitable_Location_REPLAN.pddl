(define (problem store-keychain)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    drawer1 - object
    armchair1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 armchair1)
    (holding robot1 keychain)
    (object-close robot1 drawer1)
  )

  (:goal (and
    (at-location keychain drawer1)
    (object-close robot1 drawer1)
  ))

  (:metric minimize (total-cost))
)