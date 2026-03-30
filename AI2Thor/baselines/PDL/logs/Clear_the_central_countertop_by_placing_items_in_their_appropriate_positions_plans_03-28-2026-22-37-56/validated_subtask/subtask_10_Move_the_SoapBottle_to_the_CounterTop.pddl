(define (problem move-soapbottle-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    soapbottle - object
    countertop - object
    countertop3 - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location soapbottle countertop)
    (at-location countertop3 floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location soapbottle countertop3)
  ))

  (:metric minimize (total-cost))
)