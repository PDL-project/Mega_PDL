(define (problem place-spoon-in-drawer)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    spoon - object
    drawer1 - object
    diningtable1 - object
    floor1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor1)
    (at-location spoon diningtable1)
    (at-location drawer1 floor1)
    (object-close robot1 drawer1)
    (holding robot1 fork)
  )

  (:goal (and
    (at-location spoon drawer1)
    (object-close robot1 drawer1)
    (hand-empty robot1)
  ))

  (:metric minimize (total-cost))
)