(define (problem move-soapbottle-to-sink)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    soapbottle - object
    sink - object
    countertop - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location soapbottle countertop)
    (at-location sink floor)
    (is-sink sink)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location soapbottle sink)
  ))

  (:metric minimize (total-cost))
)