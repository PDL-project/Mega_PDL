(define (problem move-pan-to-stoveburner1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pan - object
    stoveburner1 - object
    floor - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pan floor)
    (not (holding robot1 pan))
    (not (object-close robot1 stoveburner1))
  )

  (:goal (and
    (at-location pan stoveburner1)
  ))

  (:metric minimize (total-cost))
)