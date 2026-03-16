(define (problem place-pencil-on-sidetable)
  (:domain allactionrobot)

  (:objects
    robot2 - robot
    pencil - object
    sidetable1 - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot2))
    (holding robot2 pencil)
    (at robot2 sidetable1)
    (not (object-close robot2 sidetable1))
  )

  (:goal (and
    (at-location pencil sidetable1)
  ))

  (:metric minimize (total-cost))
)