(define (problem close-cabinet6)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet6 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location cabinet6 floor)
    (object-open robot1 cabinet6)
  )

  (:goal (and
    (object-close robot1 cabinet6)
  ))

  (:metric minimize (total-cost))
)