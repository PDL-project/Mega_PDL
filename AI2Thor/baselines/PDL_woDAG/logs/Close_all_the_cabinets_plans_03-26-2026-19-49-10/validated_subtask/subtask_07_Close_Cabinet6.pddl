(define (problem close-cabinet6)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet6 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location cabinet6 floor)
    (object-open robot1 cabinet6)
    (= (total-cost) 0)
  )

  (:goal (and
    (object-close robot1 cabinet6)
  ))

  (:metric minimize (total-cost))
)