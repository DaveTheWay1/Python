# Class Attributes
# class BankAccount:
#     # Declaring a class attribute
#     # Shared among all bank accounts
#     # bank_name = "First National Dojo"		
    
#     def __init__(self, int_rate, balance):
#         self.int_rate = int_rate
#         self.balance = balance

#     # but you can change them on an instance
#     adriensAccount = BankAccount()
#     sadiesAccount = BankAccount()
#     adriensAccount.bank_name = "Dojo Credit Union"
        
#     print(adriensAccount.bank_name)
#     # output: Dojo Credit Union
        
#     print(sadiesAccount.bank_name)
#     # output: First National Dojo
    
#     # changing them on a class
#     BankAccount.bank_name = "Bank of Dojo"
    
#     print(adriensAccount.bank_name)
#     # output: Bank of Dojo
        
#     print(sadiesAccount.bank_name)
    # output: Bank of Dojo

    # classmethod

class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []
    
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum

    # staticmethods
    class BankAccount:
    # ... __init__ goes here
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True