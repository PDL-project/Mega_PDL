```pddl
(define (problem slice-tomato)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    knife - object
    countertop - object
    drawer - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)

    (at-location tomato countertop)
    (at-location knife drawer)

    (object-close robot1 drawer)
  )

  (:goal (and
    (sliced tomato)
  ))
)
```