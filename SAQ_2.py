class BankAccount:
    def __init__(self, balance=0):
        # Encapsulation: As we are using private attribute with dunder
        self.__balance = balance

    def deposit_amount(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw_amount(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    # Abstraction: hiding the internal details and implementation
    def check_balance(self):
        return f"\nAvailable Balance: {self.__balance}"


#Implementation part of the program

bank_account = BankAccount(1000)
bank_account.deposit_amount(200)
bank_account.withdraw_amount(100)

#printing the information
print(bank_account.check_balance())
