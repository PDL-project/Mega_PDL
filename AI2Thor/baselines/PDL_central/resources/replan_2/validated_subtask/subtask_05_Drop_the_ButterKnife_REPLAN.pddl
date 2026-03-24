(define (problem drop-butterknife)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterknife - object
    bowl1 - object
    kitchen - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 butterknife)
    (at-location bowl1 kitchen)
    (not (object-close robot1 bowl1))
  )

  (:goal (and
    (at-location butterknife bowl1)
    (not (holding robot1 butterknife))
  ))

  (:metric minimize (total-cost))
)