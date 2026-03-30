```pddl
(define (problem slice-bread)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    knife - object
    bread - object
    countertop - object
    kitchen - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)

    (at-location knife countertop)
    (at-location bread countertop)

    (not (holding robot1 knife))
    (not (holding robot1 bread))
  )

  (:goal (and
    (sliced bread)
    (at-location bread countertop)
  ))
)
```