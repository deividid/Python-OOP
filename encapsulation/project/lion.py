from project.animal import Animal


class Lion(Animal):
    def __init__(self, name, gender, money):
        super().__init__(name, gender, money, 50)


