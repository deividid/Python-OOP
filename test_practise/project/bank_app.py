from typing import List

from test_practise.project.clients.base_client import BaseClient
from test_practise.project.loans.base_loan import BaseLoan


class BankApp:
    def __init__(self, capacity):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    types = {"Loans": ["StudentLoan", "MortgageLoan"], "Clients": ["Student", "Adult"]}

    def add_loan(self, loan_type: BaseLoan):
        if loan_type not in BankApp.types["Loans"]:
            raise Exception("Invalid loan type!")
        self.loans.append(loan_type())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: BaseClient, client_name, client_id, income):
        if client_type not in BankApp.types["Clients"]:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        self.clients.append(client_type(client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                if (client.__class__.name == "Student" and loan_type != "StudentLoan") or (client.__class__.name == "Adult" and loan_type != "MortgageLoan"):
                    raise Exception("Inappropriate loan type!")

                else:
                    for loan in self.loans:
                        if loan.__class__.__name__ == loan_type:
                            client.loans.append(loan)
                            self.loans.remove(loan)
                            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id):
        if client_id not in [c.client_id for c in self.clients]:
            raise Exception("No such client!")

        if len([c.loans for c in self.clients if c.client_id == client_id]) != 0:
            raise Exception("The client has loans! Removal is impossible!")

        for client in self.clients:
            if client.client_id == client_id:
                self.clients.remove(client)
                return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        count = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                count += 1

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate):
        count = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        result = f"Active Clients: {len(self.clients):.2f}\nTotal Income: {sum([c.income for c in self.clients]):.2f}\n"
        client_loans_count = 0
        client_loans_sum = 0
        total_client_interest: float = 0.0
        total_bank_loans = 0
        total_sum_of_bank_loans = 0
        for c in self.clients:
            client_loans_sum += sum(c.loans)
            client_loans_count += len(c.loans)
            total_client_interest += c.interest

        for l in self.loans:
            total_sum_of_bank_loans += l.amount
            total_bank_loans += 1

        result += f"Granted Loans: {client_loans_count:.2f}, Total Sum: {client_loans_sum:.2f}\n" \
                  f"Available Loans: {total_bank_loans:.2f}, Total Sum: {total_sum_of_bank_loans:.2f}\n" \
                  f"Average Client Interest Rate: {(total_client_interest / len(self.clients)):.2f}"







