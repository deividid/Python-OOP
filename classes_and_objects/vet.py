class Vet:
    def __init__(self, name):
        self.name = name
        self.animals = []

    animals = []
    space = 5

    def register_animal(self, animal_name):
        if Vet.space > 0:
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            Vet.space -= 1
            return f"{animal_name} registered in the clinic"

        else:
            return f"Not enough space"

    def unregister_animal(self, name):
        if name in self.animals:
            self.animals.remove(name)
            Vet.animals.remove(name)
            Vet.space += 1
            return f"{name} unregistered successfully"

        else:
            return f"{name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"

peter = Vet("Peter")

george = Vet("George")

print(peter.register_animal("Tom"))

print(george.register_animal("Cory"))

print(peter.register_animal("Fishy"))

print(peter.register_animal("Bobby"))

print(george.register_animal("Kay"))

print(george.unregister_animal("Cory"))

print(peter.register_animal("Silky"))

print(peter.unregister_animal("Molly"))

print(peter.unregister_animal("Tom"))

print(peter.info())

print(george.info())
