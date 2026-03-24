(define (problem close-cabinet2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet2 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cabinet2 floor)
    (object-open robot1 cabinet2)
  )

  (:goal (and
    (object-close robot1 cabinet2)
  ))

  (:metric minimize (total-cost))
)