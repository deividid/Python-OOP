from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name, gender, money):
        super().__init__(name, gender, money, 45)
