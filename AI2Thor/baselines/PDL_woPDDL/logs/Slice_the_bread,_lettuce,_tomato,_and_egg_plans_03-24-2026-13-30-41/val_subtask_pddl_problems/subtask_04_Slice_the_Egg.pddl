(define (problem slice-egg)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    egg - object
    butterknife - object
    countertop - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location egg countertop)
    (at-location butterknife countertop)

    (not (holding robot1 egg))
    (not (holding robot1 butterknife))

    (not (object-close robot1 countertop))
  )

  (:goal (and
    (sliced egg)
    (at-location egg countertop)
  ))

  (:metric minimize (total-cost))
)