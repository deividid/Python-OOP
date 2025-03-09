from project.animal import Animal
from project.worker import Worker

class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        else:
            return "Not enough space for worker"

    def fire_worker(self, worker):

        for x in self.workers:
            if worker == x.name:
                self.workers.remove(x)

                return f"{worker} fired successfully"


        return f"There is no {worker} in the zoo"

    def pay_workers(self):
        money_needed = sum([cash.salary for cash in self.workers])
        if money_needed <= self.__budget:
            self.__budget -= money_needed
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_needed = sum([cash.money_for_care for cash in self.animals])
        if self.__budget >= money_needed:
            self.__budget -= money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"

        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [x for x in self.workers if x.__class__.__name__ == "Keeper"]
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"

        caretakers = [x for x in self.workers if x.__class__.__name__ == "Caretaker"]
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"

        vets = [x for x in self.workers if x.__class__.__name__ == "Vet"]
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += f"{vet}\n"

        return result[:-1]


