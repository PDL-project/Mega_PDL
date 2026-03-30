(define (problem put-watch-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    watch - object
    sidetable1 - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location watch sidetable1)
    (at-location sofa floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location watch sofa)
  ))

  (:metric minimize (total-cost))
)