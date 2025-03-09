from project.food import Food


class Fruit(Food):
    def __init__(self, name, date):
        self.name = name
        super().__init__(date)

        