(define (problem put-butterknife-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    countertop1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location butterknife floor)
    (at-location countertop1 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location butterknife countertop1)
  ))

  (:metric minimize (total-cost))
)