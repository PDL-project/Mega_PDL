(define (problem move-pencil-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    sofa - object
    sidetable - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pencil sofa)
    (at-location sidetable floor)
    (not (holding robot1 pencil))
    (object-close robot1 sofa)
  )

  (:goal (and
    (at-location pencil sidetable)
    (not (holding robot1 pencil))
  ))

  (:metric minimize (total-cost))
)