(define (problem put-butterknife-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterKnife - object
    counterTop - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location butterKnife floor)
    (at-location counterTop floor)
    (not (holding robot1 butterKnife))
  )

  (:goal (and
    (at-location butterKnife counterTop)
    (not (holding robot1 butterKnife))
  ))

  (:metric minimize (total-cost))
)