from test_practise.project.clients.base_client import BaseClient


class Adult(BaseClient):
    def __init__(self, name, client_id, income):
        super().__init__(name, client_id, income, 4.0)

    def increase_clients_interest(self):
        self.interest += 2.0
