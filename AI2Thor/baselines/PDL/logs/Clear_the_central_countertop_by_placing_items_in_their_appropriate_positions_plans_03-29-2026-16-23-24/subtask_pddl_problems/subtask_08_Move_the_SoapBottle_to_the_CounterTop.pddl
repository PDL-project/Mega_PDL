```pddl
(define (problem move-soapbottle-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    soapbottle - object
    countertop - object
    countertop2 - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 floor)
    (hand-empty robot1)
    (at-location soapbottle countertop)
    (at-location countertop2 floor)
  )

  (:goal (and
    (at-location soapbottle countertop2)
  ))
)
```