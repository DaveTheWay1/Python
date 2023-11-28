# This means that the User class, instead of directly 
# having a balance attribute, will now have an attribute 
# of type BankAccount. To establish this relationship, 
# we can update our User's __init__ method to something like this, 
# removing the account_balance attribute and adding an account attribute:
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.04
        self.balance = 0
        # BankAccount.all_accounts.append(self)
        # pass

    def deposit(self, amount):
        self.balance += amount
        print(f"New Account Balance: ${self.balance}")
        return self

    def with_draw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"New Account Balance With Withdraw: ${self.balance}")
            return self
        elif self.balance < amount:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= amount
            self.balance -= 5
            print(f"New Account Balance: {self.balance}")
            return self

    def display_account_info(self):
        print(f"Account Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            x = self.balance * self.int_rate
            print(f"Total From Interest Rate ${x}")
            self.balance += x
            print(f"New Account Balance With Interest Rate: ${self.balance}")
            return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line

david = User("david", "ramirez@gmail.com")

david.account.deposit(100)
# or access its attributes
print(david.account.balance)