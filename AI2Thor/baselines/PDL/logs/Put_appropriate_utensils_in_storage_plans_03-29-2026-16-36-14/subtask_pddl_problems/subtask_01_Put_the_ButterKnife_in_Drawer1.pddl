```lisp
(define (problem put-butterknife-in-drawer1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    drawer - object
    drawer1 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location butterknife drawer)
    (at-location drawer1 floor)
    (object-close robot1 drawer1)
  )

  (:goal (and
    (at-location butterknife drawer1)
    (object-close robot1 drawer1)
  ))
)
```