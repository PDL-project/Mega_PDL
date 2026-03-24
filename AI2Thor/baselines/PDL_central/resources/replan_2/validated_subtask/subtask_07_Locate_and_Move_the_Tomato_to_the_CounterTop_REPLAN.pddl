(define (problem move-tomato-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    butterknife - object
    drawer1 - object
    countertop1 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (holding robot1 butterknife)
    (at-location tomato floor)
    (at-location drawer1 floor)
    (at-location countertop1 floor)

    (object-open robot1 drawer1)
  )

  (:goal (and
    (at-location tomato countertop1)
  ))

  (:metric minimize (total-cost))
)