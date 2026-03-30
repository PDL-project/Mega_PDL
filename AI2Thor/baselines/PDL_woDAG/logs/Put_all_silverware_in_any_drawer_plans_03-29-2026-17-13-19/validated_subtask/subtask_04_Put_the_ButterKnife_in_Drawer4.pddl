(define (problem put-butterknife-in-drawer4)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterKnife - object
    drawer4 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location butterKnife countertop)
    (at-location drawer4 floor)
    (object-close robot1 drawer4)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location butterKnife drawer4)
    (object-close robot1 drawer4)
  ))

  (:metric minimize (total-cost))
)