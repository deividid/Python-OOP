from project.animals.animal import Mammal

from project.food import Food


class Mouse(Mammal):

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat" or food.__class__.__name__ == "Seed":
            return f"{Mouse.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.1 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{Dog.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.4 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Fruits" or food.__class__.__name__ == "Seed":
            return f"{Cat.__name__} does not eat {food.__class__.__name__}!"

        self.weight += 0.3 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{Tiger.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity
        self.food_eaten += food.quantity
