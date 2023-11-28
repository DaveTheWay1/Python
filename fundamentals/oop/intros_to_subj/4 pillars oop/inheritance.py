
# * The below shows how a parent class gets passed in
# * Simply putting the parent class within the parenthesis connects the two
# * this is ofc assuming the BankAccount class is somewhere and complete
#  class CheckingAccount(BankAccount):
#     pass   

# * The below is two classes done how we have been doing them
# * But as you may notice the share a few attributes
# ! repeating code.... oh no!

# class BankAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance

# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#         self.is_roth = is_roth  

# * This is where super() comes in. To help us not repeat 
# * code between parents and child classes
# * super helps us get what we need passed from the parent class.

class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)	
        self.is_roth = is_roth	

# * the below is an exmaple of adding logic without super
class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

# * this is with super() invovled
class BankAccount:
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

class RetirementAccount(BankAccount):
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self
