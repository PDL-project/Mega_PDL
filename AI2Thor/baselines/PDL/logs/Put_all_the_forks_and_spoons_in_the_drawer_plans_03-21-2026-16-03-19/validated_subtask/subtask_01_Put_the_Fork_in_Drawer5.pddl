(define (problem put-fork-in-drawer5)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    drawer5 - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location fork countertop)
    (at-location drawer5 floor)
    (object-close robot1 drawer5)
    (not (holding robot1 fork))
  )

  (:goal (and
    (at-location fork drawer5)
    (object-close robot1 drawer5)
  ))

  (:metric minimize (total-cost))
)