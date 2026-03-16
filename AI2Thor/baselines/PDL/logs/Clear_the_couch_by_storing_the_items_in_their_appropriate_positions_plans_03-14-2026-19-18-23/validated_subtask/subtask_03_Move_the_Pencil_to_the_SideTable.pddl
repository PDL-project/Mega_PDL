(define (problem move-pencil-to-sidetable)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pencil - object
    sidetable - object
    sofa - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pencil sofa)
    (at-location sidetable floor)
    (not (holding robot1 pencil))
    (not (object-close robot1 sidetable))
  )

  (:goal (and
    (at-location pencil sidetable)
    (not (holding robot1 pencil))
  ))

  (:metric minimize (total-cost))
)