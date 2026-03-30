(define (problem move-soapbottle-to-countertop3)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    soapbottle - object
    countertop3 - object
    countertop2 - object
    bread - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 countertop2)
    (holding robot1 bread)
    (at-location soapbottle floor)
    (at-location bread countertop2)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location soapbottle countertop3)
  ))

  (:metric minimize (total-cost))
)