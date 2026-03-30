(define (problem locate-and-approach-pot)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pot - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (= (total-cost) 0)
  )

  (:goal (and
    (at robot1 pot)
  ))

  (:metric minimize (total-cost))
)