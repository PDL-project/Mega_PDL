```pddl
(define (problem clean-the-cup)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    cup - object
    sink - object
    floor - object
    faucet - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (at-location cup floor)
    (at-location sink floor)
    (at-location faucet floor)

    (is-sink sink)
    (is-faucet faucet)

    (not (holding robot1 cup))
    (not (faucet-on))
  )

  (:goal (and
    (cleaned robot1 cup)
    (at-location cup floor)
  ))
)
```