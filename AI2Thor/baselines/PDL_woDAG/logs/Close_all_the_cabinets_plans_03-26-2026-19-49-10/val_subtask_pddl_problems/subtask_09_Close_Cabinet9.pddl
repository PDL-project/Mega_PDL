(define (problem close-cabinet9)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cabinet9 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location cabinet9 floor)
  )

  (:goal (and
    (object-close robot1 cabinet9)
  ))

  (:metric minimize (total-cost))
)