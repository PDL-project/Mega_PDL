(define (problem move-fork-to-drawer3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    drawer2 - object
    drawer3 - object
    countertop2 - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location fork countertop2)
    (at-location drawer2 floor)
    (at-location drawer3 floor)

    (object-close robot1 drawer2)
    (not (object-close robot1 drawer3))

    (not (holding robot1 fork))
  )

  (:goal (and
    (at-location fork drawer3)
    (object-close robot1 drawer3)
  ))

  (:metric minimize (total-cost))
)