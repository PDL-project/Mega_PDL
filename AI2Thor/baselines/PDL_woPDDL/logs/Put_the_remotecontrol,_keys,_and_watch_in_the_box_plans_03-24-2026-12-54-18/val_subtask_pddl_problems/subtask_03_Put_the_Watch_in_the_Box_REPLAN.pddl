(define (problem put-watch-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    watch - object
    box - object
    sidetable3 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 box)
    (holding robot1 KeyChain)
    (object-close robot1 box)
    (at-location watch sidetable3)
  )

  (:goal (and
    (at-location watch box)
    (object-close robot1 box)
  ))

  (:metric minimize (total-cost))
)