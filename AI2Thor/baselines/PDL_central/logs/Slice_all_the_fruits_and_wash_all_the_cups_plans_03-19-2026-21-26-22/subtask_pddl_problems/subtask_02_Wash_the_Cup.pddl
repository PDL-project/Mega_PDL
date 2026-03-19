```pddl
(define (problem wash-the-cup)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cup - object
    cabinet - object
    sink - object
    countertop - object
    floor - object
    sinkbasin - object
    faucet - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location cup cabinet)
    (at-location cabinet floor)
    (at-location sink floor)
    (at-location countertop floor)

    (object-close robot1 cabinet)

    (not (holding robot1 cup))
    (not (cleaned robot1 cup))

    (is-sink sinkbasin)
    (is-faucet faucet)
    (not (switch-on robot1 faucet))
  )

  (:goal (and
    (cleaned robot1 cup)
    (at-location cup countertop)
    (not (holding robot1 cup))
  ))
)
```