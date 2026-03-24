(define (problem turn-on-stoveknob3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    stoveknob3 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location stoveknob3 floor)
    (switch-off robot1 stoveknob3)
  )

  (:goal (and
    (switch-on robot1 stoveknob3)
  ))

  (:metric minimize (total-cost))
)