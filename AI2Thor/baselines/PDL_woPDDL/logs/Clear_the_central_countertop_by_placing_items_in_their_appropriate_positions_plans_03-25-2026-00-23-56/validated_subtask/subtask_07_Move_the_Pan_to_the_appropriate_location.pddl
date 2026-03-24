(define (problem move-pan-to-stove)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pan - object
    stoveburner1 - object
    countertop - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pan countertop)
    (at-location stoveburner1 floor)
    (not (holding robot1 pan))
  )

  (:goal (and
    (at-location pan stoveburner1)
    (not (holding robot1 pan))
  ))

  (:metric minimize (total-cost))
)