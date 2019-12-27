class Account:

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __get_name__(self):
        return self.name

    def __set_name__(self, name):
        self.name = name

    def __get_pin__(self):
        return self.pin

    def __set_pin__(self, pin):
        self.pin = pin

    def __get_balance__(self):
        return self.balance

    def __set_balance__(self, balance):
        self.balance = balance

    def _deposit(self, deposition_amount):
        self.balance += deposition_amount

    def _withdraw(self, withdrawal_amount):
        self.balance -= withdrawal_amount
