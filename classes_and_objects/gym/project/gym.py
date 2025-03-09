from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer




class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.equipment: List[Equipment] = []
        self.trainers: List[Trainer] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, c: Customer):
        if c not in self.customers:

            self.customers.append(c)

    def add_equipment(self, e:Equipment):
        if e not in self.equipment:
            self.equipment.append(e)

    def add_trainer(self, t:Trainer):
        if t not in self.trainers:
            self.trainers.append(t)

    def add_plan(self, p:ExercisePlan):
        if p not in self.plans:
            self.plans.append(p)

    def add_subscription(self, s:Subscription):
        if s not in self.subscriptions:
            self.subscriptions.append(s)

    def subscription_info(self, subscription_id):
        idx = subscription_id - 1
        return f"{self.subscriptions[idx]}\n{self.customers[idx]}\n{self.trainers[idx]}\n{self.equipment[idx]}\n{self.plans[idx]}"





