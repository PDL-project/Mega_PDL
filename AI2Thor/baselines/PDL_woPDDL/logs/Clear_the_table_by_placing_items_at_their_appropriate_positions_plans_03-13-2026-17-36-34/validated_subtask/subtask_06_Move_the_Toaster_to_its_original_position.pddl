(define (problem move-toaster-to-original-position)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    toaster - object
    diningtable - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location toaster diningtable)
    (not (holding robot1 toaster))
  )

  (:goal (and
    (at-location toaster diningtable)
    (not (holding robot1 toaster))
  ))

  (:metric minimize (total-cost))
)