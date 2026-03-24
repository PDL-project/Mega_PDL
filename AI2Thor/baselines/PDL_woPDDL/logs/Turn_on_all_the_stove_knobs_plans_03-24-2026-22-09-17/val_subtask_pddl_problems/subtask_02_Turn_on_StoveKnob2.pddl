(define (problem turn-on-stoveknob2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    stoveknob2 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location stoveknob2 floor)
    (switch-off robot1 stoveknob2)
  )

  (:goal (and
    (switch-on robot1 stoveknob2)
  ))

  (:metric minimize (total-cost))
)