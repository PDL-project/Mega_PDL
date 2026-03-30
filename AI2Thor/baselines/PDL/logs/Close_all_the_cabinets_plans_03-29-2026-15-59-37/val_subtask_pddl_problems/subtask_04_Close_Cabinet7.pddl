(define (problem close-cabinet7)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet7 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location cabinet7 floor)
    (object-open robot1 cabinet7)
    (= (total-cost) 0)
  )

  (:goal (and
    (object-close robot1 cabinet7)
  ))

  (:metric minimize (total-cost))
)