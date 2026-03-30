(define (problem move-book-to-sofa)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    book - object
    diningtable - object
    sofa - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location book diningtable)
    (at-location sofa floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location book sofa)
  ))

  (:metric minimize (total-cost))
)