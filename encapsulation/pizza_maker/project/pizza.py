from project.dough import Dough

from project.topping import Topping


class Pizza(Dough, Topping):
    def __init__(self, name: str, dough: Dough, max_number_of_toppings):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    double_counting = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")

        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value
    
    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings
    
    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.__max_number_of_toppings - self.double_counting:
            raise ValueError("Not enough space for another topping")
        name = topping.topping_type
        weight = topping.weight
        if name in self.toppings.keys():
            self.toppings[name] += weight
            self.double_counting += 1

        else:

            self.toppings[name] = weight

    def calculate_total_weight(self):
        result = self.dough.weight
        for keys, value in self.toppings.items():
            result += value

        return result

