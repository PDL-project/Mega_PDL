(define (problem put-butterknife-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterKnife - object
    drawer2 - object
    countertop1 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 countertop1)
    (at-location butterKnife countertop1)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location butterKnife drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)