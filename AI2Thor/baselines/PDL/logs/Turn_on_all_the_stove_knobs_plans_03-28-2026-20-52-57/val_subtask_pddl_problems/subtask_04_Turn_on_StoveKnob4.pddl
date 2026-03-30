(define (problem turn-on-stoveknob4)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    stoveknob4 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location stoveknob4 floor)
    (switch-off robot1 stoveknob4)
    (= (total-cost) 0)
  )

  (:goal (and
    (switch-on robot1 stoveknob4)
  ))

  (:metric minimize (total-cost))
)