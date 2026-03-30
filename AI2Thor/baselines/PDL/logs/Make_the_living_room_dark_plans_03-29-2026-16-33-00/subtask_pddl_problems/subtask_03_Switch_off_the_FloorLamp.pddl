```lisp
(define (problem switch-off-floorlamp)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    floorlamp - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location floorlamp floor)
    (switch-on robot1 floorlamp)
  )

  (:goal (and
    (switch-off robot1 floorlamp)
  ))
)
```