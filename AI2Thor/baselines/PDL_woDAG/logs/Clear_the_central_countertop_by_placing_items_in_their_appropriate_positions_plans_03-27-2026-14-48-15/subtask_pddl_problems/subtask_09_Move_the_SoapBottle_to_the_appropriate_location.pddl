```pddl
(define (problem move-soapbottle-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    soapbottle - object
    sink - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location soapbottle countertop)
    (at-location sink floor)
    (is-sink sink)
  )

  (:goal (and
    (at-location soapbottle sink)
  ))
)
```