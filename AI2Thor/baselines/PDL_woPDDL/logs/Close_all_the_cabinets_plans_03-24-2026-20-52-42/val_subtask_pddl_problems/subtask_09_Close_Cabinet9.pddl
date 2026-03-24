(define (problem close-cabinet9)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet9 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cabinet9 floor)
    (object-open robot1 cabinet9)
  )

  (:goal (and
    (object-close robot1 cabinet9)
  ))

  (:metric minimize (total-cost))
)