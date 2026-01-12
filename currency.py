class Currency:
    def __init__(self, balance):
        self.balance = balance  # stored value

# update balance by adding/subtract the amount provided when called
    def add(self, amount):
        self.balance += amount

    def subtract(self, amount):
        self.balance -= amount

    def __str__(self):
        return f'Balance: ${self.balance}'


money1 = Currency(100)

print(money1)

money1.add(50)

print(money1)
