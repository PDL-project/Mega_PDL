(define (problem put-watch-in-box)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    watch - object
    box - object
    sidetable - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location watch sidetable)
    (at-location box floor)
    (not (holding robot1 watch))
    (object-close robot1 box)
  )

  (:goal (and
    (at-location watch box)
    (object-close robot1 box)
  ))

  (:metric minimize (total-cost))
)