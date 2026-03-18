(define (problem move-pen-to-side-table)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    pen - object
    sofa - object
    sidetable - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location pen sofa)
    (at-location sidetable floor)
    (not (holding robot1 pen))
    (object-close robot1 sidetable) ;; sidetable is openable, starts closed
  )

  (:goal (and
    (at-location pen sidetable)
    (object-close robot1 sidetable) ;; ensure sidetable is closed after placing the pen
  ))

  (:metric minimize (total-cost))
)