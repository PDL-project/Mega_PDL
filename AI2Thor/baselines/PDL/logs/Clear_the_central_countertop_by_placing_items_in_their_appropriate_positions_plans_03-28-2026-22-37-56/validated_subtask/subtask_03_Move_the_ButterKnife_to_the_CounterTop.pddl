(define (problem move-butterknife-to-countertop)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    butterKnife - object
    CounterTop - object
    CounterTop2 - object
    kitchen - object
    Floor - object
  )

  (:init
    (not (inaction robot1))
    (at robot1 kitchen)
    (hand-empty robot1)
    (at-location butterKnife CounterTop)
    (at-location CounterTop2 Floor)
    (= (total-cost) 0)
  )

  (:goal (and
    (at-location butterKnife CounterTop2)
  ))

  (:metric minimize (total-cost))
)