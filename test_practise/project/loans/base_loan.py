from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate: float, amount: float):
        self.amount = amount
        self.interest_rate = interest_rate

    def increase_interest_rate(self):
        pass
