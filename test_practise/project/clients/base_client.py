from abc import ABC, abstractmethod
from typing import List

from test_practise.project.loans.base_loan import BaseLoan


class BaseClient(ABC):
    def __init__(self, name, client_id, income, interest: float):
        self.name = name
        self.client_id = client_id
        self.income = income
        self.interest: float = interest
        self.loans: List[BaseLoan] = []
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Client name cannot be empty!")
        self.__name = value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        if len(value) != 10:
            raise ValueError("Client ID should be 10 symbols long!")
        self.__client_id = value
        
    @property
    def income(self):
        return self.__income
    
    @income.setter
    def income(self, value):
        if value <= 0:
            raise ValueError("Income must be greater than zero!")
        self.__income = value

    def increase_clients_interest(self):
        pass
