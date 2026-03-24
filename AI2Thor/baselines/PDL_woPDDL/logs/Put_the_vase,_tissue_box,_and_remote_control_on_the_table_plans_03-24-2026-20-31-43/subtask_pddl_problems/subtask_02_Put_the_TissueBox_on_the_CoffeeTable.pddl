```pddl
(define (problem put-tissuebox-on-coffeetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tissuebox - object
    tvstand - object
    coffeetable - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location tissuebox tvstand)
    (at-location coffeetable floor)
    (not (holding robot1 tissuebox))
  )

  (:goal (and
    (at-location tissuebox coffeetable)
    (not (holding robot1 tissuebox))
  ))
)
```