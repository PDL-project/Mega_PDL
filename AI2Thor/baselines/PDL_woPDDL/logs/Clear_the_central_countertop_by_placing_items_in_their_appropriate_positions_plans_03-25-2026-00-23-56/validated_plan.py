(define (problem move-apple-to-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    apple - object
    bowl - object
    countertop - object
    floor - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location apple countertop)
    (at-location bowl floor)

    (not (holding robot1 apple))
  )

  (:goal (and
    (at-location apple bowl)
    (not (holding robot1 apple))
  ))
)