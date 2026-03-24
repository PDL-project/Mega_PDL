(define (problem move-soapbottle-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    soapbottle - object
    countertop - object
    sink - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location soapbottle countertop)
    (is-sink sink)
    (not (holding robot1 soapbottle))
    (not (faucet-on))
  )

  (:goal (and
    (at-location soapbottle sink)
  ))

  (:metric minimize (total-cost))
)