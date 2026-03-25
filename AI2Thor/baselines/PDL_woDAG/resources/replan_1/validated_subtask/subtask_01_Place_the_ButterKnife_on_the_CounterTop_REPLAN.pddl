(define (problem place-butterknife-on-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    countertop - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location butterknife floor)
    (at-location countertop floor)
    (not (holding robot1 butterknife))
  )

  (:goal (and
    (at-location butterknife countertop)
  ))

  (:metric minimize (total-cost))
)