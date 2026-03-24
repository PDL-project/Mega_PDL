(define (problem move-soapbottle-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    soapbottle - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 soapbottle)
    (at-location soapbottle floor)
    (at-location countertop floor)
    (not (holding robot1 soapbottle))
  )

  (:goal (and
    (at-location soapbottle countertop)
  ))

  (:metric minimize (total-cost))
)