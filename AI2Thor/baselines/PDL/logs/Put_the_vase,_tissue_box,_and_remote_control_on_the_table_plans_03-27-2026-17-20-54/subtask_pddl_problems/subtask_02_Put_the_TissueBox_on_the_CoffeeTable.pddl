```lisp
(define (problem put-tissuebox-on-coffeetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tissuebox - object
    tvstand - object
    coffeetable - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location tissuebox tvstand)
    (at-location coffeetable floor)
  )

  (:goal (and
    (at-location tissuebox coffeetable)
  ))
)
```