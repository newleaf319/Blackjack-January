class Currency:

    RATES = {  # dictionary stores exchange rates relative to USD
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.79
    }

    def __init__(self, balance, currency='USD'):
        self.balance = balance
        self.currency = currency

    def convert_to(self, new_currency):
        # this is how much the balance is worth in USD base rates
        usd_value = self.balance / Currency.RATES[self.currency]
        # mutiply to convert USD to the new passed in rate
        self.balance = usd_value * Currency.RATES[new_currency]
        # update the object so it knows what currency its now in
        self.currency = new_currency

    def add(self, amount):
        self.balance += amount

    def subtract(self, amount):
        self.balance -= amount

    def __str__(self):
        return f'Balance: ${round(self.balance,2)} {self.currency}'
