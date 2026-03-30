(define (problem close-cabinet4)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet4 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location cabinet4 floor)
    (object-open robot1 cabinet4)
    (= (total-cost) 0)
  )

  (:goal (and
    (object-close robot1 cabinet4)
  ))

  (:metric minimize (total-cost))
)