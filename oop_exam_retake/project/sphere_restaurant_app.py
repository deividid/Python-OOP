from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    types_of_waiters = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    types_of_clients = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.types_of_waiters.keys():
            return f"{waiter_type} is not a recognized waiter type."

        if waiter_name in [w.name for w in self.waiters]:
            return f"{waiter_name} is already on the staff."

        new_waiter = self.types_of_waiters[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.types_of_clients.keys():
            return f"{client_type} is not a recognized client type."

        if client_name in [c.name for c in self.clients]:
            return f"{client_name} is already a client."

        new_client = self.types_of_clients[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        for w in self.waiters:
            if w.name == waiter_name:
                return w.report_shift()
        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        for c in self.clients:
            if c.name == client_name:
                return f"{client_name} earned {c.earning_points(order_amount)} points from the order."

        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        for c in self.clients:
            if c.name == client_name:
                return f"{client_name} received a {c.apply_discount()[0]}% discount. " \
                       f"Remaining points {c.apply_discount()[1]}"

        return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        result = f"$$ Monthly Report $$\nTotal Earnings: ${sum([w.calculate_earnings() for w in self.waiters]):.2f}\n" \
                 f"Total Clients Unused Points: {sum([c.points for c in self.clients])}\n" \
                 f"Total Clients Count: {len(self.clients)}"

        sorted_waiters = sorted(self.waiters, key=lambda w: (-w.calculate_earnings()))
        result += f"\n** Waiter Details **"

        for waiter in sorted_waiters:
            result += f"\n{waiter.__str__()}"

        return result
