(define (problem turn-on-stoveknob1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    stoveknob1 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location stoveknob1 floor)
    (switch-off robot1 stoveknob1)
  )

  (:goal (and
    (switch-on robot1 stoveknob1)
  ))

  (:metric minimize (total-cost))
)