(define (problem put-book-on-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    book - object
    chair - object
    sofa - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location book chair)
    (at-location sofa floor)
    (not (holding robot1 book))
  )

  (:goal (and
    (at-location book sofa)
    (not (holding robot1 book))
  ))

  (:metric minimize (total-cost))
)