(define (problem put-tissuebox-on-tvstand)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tissuebox - object
    tvstand - object
    kitchen - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location tissuebox floor)
    (at-location tvstand floor)
    (not (holding robot1 tissuebox))
  )

  (:goal (and
    (at-location tissuebox tvstand)
    (not (holding robot1 tissuebox))
  ))

  (:metric minimize (total-cost))
)