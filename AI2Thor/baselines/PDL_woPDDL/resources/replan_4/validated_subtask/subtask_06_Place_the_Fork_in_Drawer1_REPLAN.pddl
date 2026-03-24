(define (problem place-fork-in-drawer3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    drawer3 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location fork floor)
    (at-location drawer3 floor)

    (not (holding robot1 fork))
    (object-close robot1 drawer3)
  )

  (:goal (and
    (at-location fork drawer3)
    (object-close robot1 drawer3)
  ))

  (:metric minimize (total-cost))
)