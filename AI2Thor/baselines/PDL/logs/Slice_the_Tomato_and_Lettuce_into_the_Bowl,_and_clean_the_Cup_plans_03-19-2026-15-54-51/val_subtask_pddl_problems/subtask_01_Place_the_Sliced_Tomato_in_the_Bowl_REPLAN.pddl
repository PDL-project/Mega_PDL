(define (problem place-sliced-tomato-in-bowl)
  (:domain allactionrobot)

  (:objects
    robot1 - robot
    TomatoSliced - object
    bowl1 - object
    kitchen - object
    CounterTop - object
  )

  (:init
    (= (total-cost) 0)
    (not (inaction robot1))
    (at robot1 kitchen)
    (holding robot1 TomatoSliced)
    (at-location bowl1 CounterTop)
    (at robot1 bowl1)
  )

  (:goal (and
    (at-location TomatoSliced bowl1)
    (not (holding robot1 TomatoSliced))
  ))

  (:metric minimize (total-cost))
)