class Account:
    def __init__(self, owner, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction):
        if self.amount + + sum(self._transactions) + transaction < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            self._transactions.append(transaction)
            return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        return self.handle_transaction(amount)

    @property
    def balance(self):
        total = sum(self._transactions) + self.amount
        return total

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __reversed__(self):
        return reversed(self._transactions)

    def __eq__(self, other):
        return self.amount == other.amount

    def __ne__(self, other):
        return self.amount != other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __add__(self, other):
        new_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        new_account._transactions = self._transactions + other._transactions

        return new_account

acc = Account('bob', 10)

acc2 = Account('john')

print(acc)

print(repr(acc))

acc.add_transaction(20)

acc.add_transaction(-20)

acc.add_transaction(30)

print(acc.balance)

print(len(acc))

for transaction in acc:

    print(transaction)

print(acc[1])

print(list(reversed(acc)))

acc2.add_transaction(10)

acc2.add_transaction(60)

print(acc > acc2)

print(acc >= acc2)

print(acc < acc2)

print(acc <= acc2)

print(acc == acc2)

print(acc != acc2)

acc3 = acc + acc2

print(acc3)

print(acc3._transactions)



