from polymorphism_and_abstraction.exercise_4.project.food import Vegetable, Meat, Seed, Fruit
from polymorphism_and_abstraction.exercise_4.project.animals.birds import Owl, Hen
from polymorphism_and_abstraction.exercise_4.project.animals.mammals import Dog, Cat, Tiger, Mouse





owl = Owl("Pip", 10, 10)

print(owl)

meat = Meat(4)

print(owl.make_sound())

owl.feed(meat)

veg = Vegetable(1)

print(owl.feed(veg))

print(owl)