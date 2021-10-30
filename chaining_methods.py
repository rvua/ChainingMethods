class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = 0
    def make_deposit(self, amount):
        self.amount += amount
        return self
    def make_withdrawal(self, amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}.")
        return self

richard = User("Richard", 5500)
richard.make_deposit(10).make_deposit(15).make_deposit(20).make_withdrawal(30).display_user_balance()
matt = User("Matt", 5200)
matt.make_deposit(15).make_deposit(40).make_withdrawal(30).make_withdrawal(35).display_user_balance()
luke = User("Luke", 5000)
luke.make_deposit(40).make_withdrawal(20).make_withdrawal(30).make_withdrawal(25).display_user_balance()