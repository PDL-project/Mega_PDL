(define (problem slice-bread)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    bread - object
    butterknife - object
    countertop - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location bread countertop)
    (at-location butterknife countertop)

    (not (holding robot1 bread))
    (not (holding robot1 butterknife))
  )

  (:goal (and
    (sliced bread)
    (at-location bread countertop)
  ))

  (:metric minimize (total-cost))
)