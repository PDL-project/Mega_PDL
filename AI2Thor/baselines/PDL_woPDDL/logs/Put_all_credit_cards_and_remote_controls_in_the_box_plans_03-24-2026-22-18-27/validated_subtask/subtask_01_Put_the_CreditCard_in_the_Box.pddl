(define (problem put-creditcard-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    creditcard - object
    box - object
    diningtable - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location creditcard diningtable)
    (at-location box floor)
    (object-close robot1 box)
    (not (holding robot1 creditcard))
  )

  (:goal (and
    (at-location creditcard box)
    (not (holding robot1 creditcard))
    (object-close robot1 box)
  ))

  (:metric minimize (total-cost))
)