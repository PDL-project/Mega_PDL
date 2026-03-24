(define (problem move-fork-to-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    fork - object
    drawer2 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location fork floor)
    (at-location drawer2 floor)
    (object-close robot1 drawer2)
  )

  (:goal (and
    (at-location fork drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)