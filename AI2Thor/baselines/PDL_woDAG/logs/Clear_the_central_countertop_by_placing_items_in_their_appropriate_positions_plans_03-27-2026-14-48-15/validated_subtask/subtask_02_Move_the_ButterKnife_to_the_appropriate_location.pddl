(define (problem move-butterknife)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    drawer1 - object
    countertop - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location butterknife countertop)
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