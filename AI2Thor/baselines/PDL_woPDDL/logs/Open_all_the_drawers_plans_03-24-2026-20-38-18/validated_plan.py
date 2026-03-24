(define (problem open-drawer1)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer1 - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location drawer1 floor)
    ;; Removed (object-close robot1 drawer1) because drawer1 is initially closed
  )

  (:goal (and
    (object-open robot1 drawer1)
  ))
)