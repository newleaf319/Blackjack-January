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
        self.currency = new_currency  # update the object so it knows what currency its now in

    def add(self, amount):
        self.balance += amount

    def subtract(self, amount):
        self.balance -= amount

    def __str__(self):
        return f'Balance: ${round(self.balance,2)} {self.currency}'


# show available currencies first
print(f"Available Currencies: {', '.join((Currency.RATES.keys()))}")

# user input to pick currency
start_currency = input('Choose your currency: ').upper()
start_balance = float(input('Enter starting balance: '))

# created money object
money = Currency(start_balance, start_currency)
