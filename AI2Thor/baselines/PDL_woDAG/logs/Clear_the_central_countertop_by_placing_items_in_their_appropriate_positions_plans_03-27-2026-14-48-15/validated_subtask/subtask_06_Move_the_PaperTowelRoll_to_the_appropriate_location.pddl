(define (problem move-paper-towel-roll)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    paperTowelRoll - object
    cabinet4 - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location paperTowelRoll countertop)
    (at-location cabinet4 floor)
    (object-close robot1 cabinet4)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location paperTowelRoll cabinet4)
    (object-close robot1 cabinet4)
  ))

  (:metric minimize (total-cost))
)