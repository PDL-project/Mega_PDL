```lisp
(define (problem move-paper-towel-roll)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    paperTowelRoll - object
    counterTop - object
    counterTop3 - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location paperTowelRoll counterTop)
    (at-location counterTop3 floor)
  )

  (:goal (and
    (at-location paperTowelRoll counterTop3)
  ))
)
```