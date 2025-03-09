from project.animals.animal import Bird

from project.food import Food


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{Owl.__name__} does not eat {food.__class__.__name__}!"

        else:
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
