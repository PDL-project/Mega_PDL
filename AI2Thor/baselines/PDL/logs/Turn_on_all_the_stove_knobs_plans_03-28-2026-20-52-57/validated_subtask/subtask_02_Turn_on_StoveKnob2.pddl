(define (problem turn-on-stoveknob2)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    stoveknob2 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location stoveknob2 floor)
    (switch-off robot1 stoveknob2)
    (= (total-cost) 0)
  )

  (:goal (and
    (switch-on robot1 stoveknob2)
  ))

  (:metric minimize (total-cost))
)