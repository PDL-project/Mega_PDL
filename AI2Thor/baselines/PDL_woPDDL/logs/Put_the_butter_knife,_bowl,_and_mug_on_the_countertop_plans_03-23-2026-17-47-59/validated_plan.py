(define (problem put-butterknife-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    countertop2 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location butterknife floor)
    (at-location countertop2 floor)
    (not (holding robot1 butterknife))
  )

  (:goal (and
    (at-location butterknife countertop2)
    (not (holding robot1 butterknife))
  ))
)