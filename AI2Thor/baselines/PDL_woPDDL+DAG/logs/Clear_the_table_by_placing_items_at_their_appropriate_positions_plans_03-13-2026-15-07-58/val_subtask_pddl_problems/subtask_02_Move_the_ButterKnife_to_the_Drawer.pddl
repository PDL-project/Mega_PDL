(define (problem move-butterknife-to-drawer)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterKnife - object
    drawer1 - object
    diningTable - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location butterKnife diningTable)
    (at-location drawer1 floor)

    (object-close robot1 drawer1)
    (not (holding robot1 butterKnife))
  )

  (:goal (and
    (at-location butterKnife drawer1)
    (object-close robot1 drawer1)
  ))

  (:metric minimize (total-cost))
)