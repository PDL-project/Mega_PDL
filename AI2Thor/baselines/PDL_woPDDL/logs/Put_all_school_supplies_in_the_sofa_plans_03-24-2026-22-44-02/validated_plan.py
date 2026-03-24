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
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location book chair)
    (not (holding robot1 book))
  )

  (:goal (and
    (at-location book sofa)
  ))
)