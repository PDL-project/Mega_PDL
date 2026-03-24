(define (problem slice-tomato)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    tomato - object
    butterknife - object
    countertop - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location tomato countertop)
    (at-location butterknife countertop)

    (not (holding robot1 tomato))
    (not (holding robot1 butterknife))

    (not (object-close robot1 countertop))
  )

  (:goal (and
    (sliced tomato)
  ))

  (:metric minimize (total-cost))
)