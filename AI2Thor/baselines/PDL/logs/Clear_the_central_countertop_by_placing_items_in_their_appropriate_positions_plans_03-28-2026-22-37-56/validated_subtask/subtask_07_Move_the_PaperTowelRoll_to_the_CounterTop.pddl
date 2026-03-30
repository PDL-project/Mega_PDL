(define (problem move-paper-towel-roll)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    paperTowelRoll - object
    counterTop - object
    counterTop3 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location paperTowelRoll counterTop)
    (at-location counterTop3 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location paperTowelRoll counterTop3)
  ))

  (:metric minimize (total-cost))
)