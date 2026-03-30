(define (problem move-butterknife)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    drawer1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location butterknife floor)
    (at-location drawer1 floor)
    (object-close robot1 drawer1)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location butterknife drawer1)
    (object-close robot1 drawer1)
  ))

  (:metric minimize (total-cost))
)