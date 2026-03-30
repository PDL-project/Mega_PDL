```pddl
(define (problem put-egg-in-fridge)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    egg - object
    fridge - object
    kitchen - object
    floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location egg fridge)
    (at-location fridge floor)

    (is-fridge fridge)
    (not (fridge-open fridge))
  )

  (:goal (and
    (at-location egg fridge)
    (not (fridge-open fridge))
  ))
)
```