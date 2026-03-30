(define (problem put-butterknife-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterKnife - object
    drawer2 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 countertop)
    (hand-empty robot1)
    (at-location butterKnife countertop)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location butterKnife drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)