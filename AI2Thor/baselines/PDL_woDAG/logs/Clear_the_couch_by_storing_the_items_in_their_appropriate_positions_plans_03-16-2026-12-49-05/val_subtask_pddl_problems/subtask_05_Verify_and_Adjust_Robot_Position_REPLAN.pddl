(define (problem verify-and-adjust-robot-position)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    armchair1 - object
    sidetable - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 sidetable)
  )

  (:goal (and
    (at robot1 armchair1)
  ))

  (:metric minimize (total-cost))
)