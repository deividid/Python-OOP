from math import floor

from project.clients.base_client import BaseClient


class VIPClient(BaseClient):
    def __init__(self, name):
        super().__init__(name, "VIP")

    def earning_points(self, order_amount: float):
        points = floor(order_amount / 5)
        self.points += points
        return points
