(define (problem open-drawer7)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    drawer7 - object
    floor - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 floor)
    (at-location drawer7 floor)
    ;; Removed (object-close robot1 drawer7) because drawer7 needs to be opened
  )

  (:goal (and
    (object-open robot1 drawer7)
  ))

  (:metric minimize (total-cost))
)