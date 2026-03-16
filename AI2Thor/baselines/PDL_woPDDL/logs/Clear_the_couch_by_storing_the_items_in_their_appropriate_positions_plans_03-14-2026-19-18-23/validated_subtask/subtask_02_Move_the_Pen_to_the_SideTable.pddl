(define (problem move-pen-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    sidetable - object
    sofa - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pen sofa)
    (at-location sidetable floor)
    (not (holding robot1 pen))
    (object-close robot1 sidetable)
  )

  (:goal (and
    (at-location pen sidetable)
    (object-close robot1 sidetable)
  ))

  (:metric minimize (total-cost))
)