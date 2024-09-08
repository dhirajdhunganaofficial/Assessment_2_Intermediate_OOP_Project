#defining a class named BankAccount with relevant methods and actions to be performed for an account.

class BankAccount:
    def __init__(self, student_id):
        # The private attributes are __balance and account number
        self.__balance = 0.0
        # Extracting the last 4 digits of student ID
        self.__account_number = student_id[-4:]

    #this function can be used to deposit a given amount to the existing __balance of an account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\nThe deposited amount is: {amount}")
        else:
            print("\nInvalid deposit amount.")

    #this function can be used to withdraw specified amount from the existing __balance of an account
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"\nTotal amount Withdrawn is: {amount}")
        else:
            print("\nInvalid withdrawal amount or insufficient funds.")

    #this function can be used to check the available __balance in an account
    def check_balance(self):
        return f"\nThe available balance is: {self.__balance}"

    #this function can be used to retrieve the account number of an existing account.
    def get_account_number(self):
        return f"\nAccount Number: {self.__account_number}"

#Implementation part of the program

#Assigning student id
student_id = "s20230452"

account = BankAccount(student_id)

#depositing amount in an account
account.deposit(500)
print(account.check_balance())

#withdrawing from an account
account.withdraw(100)
print(account.check_balance())

#reteieving the account number
print(account.get_account_number())
