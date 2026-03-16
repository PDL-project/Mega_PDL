(define (problem store-keychain)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    keychain - object
    armchair1 - object
    sidetable - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 sidetable)
    (holding robot1 keychain)
    (object-close robot1 armchair1)
  )

  (:goal (and
    (at-location keychain armchair1)
    (object-close robot1 armchair1)
  ))

  (:metric minimize (total-cost))
)