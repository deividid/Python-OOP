from polymorphism_and_abstraction.exercise_5.project.cat import Cat
from polymorphism_and_abstraction.exercise_5.project.dog import Dog
from polymorphism_and_abstraction.exercise_5.project.kitten import Kitten
from polymorphism_and_abstraction.exercise_5.project.tomcat import Tomcat

kitten = Kitten("Kiki", 1)

print(kitten.make_sound())

print(kitten)

cat = Cat("Johnny", 7, "Male")

print(cat.make_sound())

print(cat)