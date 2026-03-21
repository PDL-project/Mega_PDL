(define (problem place-knife-in-drawer2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    drawer2 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 drawer2)
    (holding robot1 knife)
    (at-location drawer2 floor)
    (object-open robot1 drawer2)
  )

  (:goal (and
    (at-location knife drawer2)
    (object-close robot1 drawer2)
  ))

  (:metric minimize (total-cost))
)