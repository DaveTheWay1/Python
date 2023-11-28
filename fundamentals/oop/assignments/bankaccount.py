class BankAccount:
    def __init__(self):
        self.int_rate = 0.04
        self.balance = 0
        BankAccount.all_accounts.append(self)

# * deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        print(f"New Account Balance: ${self.balance}")
        return self

# * withdraw(self, amount) - decreases the account balance by 
# * the given amount if there are sufficient funds; if 
# * there is not enough money, print a message 
# * "Insufficient funds: Charging a $5 fee" and deduct $5

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

# * display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Account Balance: ${self.balance}")
        return self

# * yield_interest(self) - increases the account balance 
# * by the current balance * the interest rate (as long as the balance is positive)

    def yield_interest(self):
        if self.balance > 0:
            x = self.balance * self.int_rate
            print(f"Total From Interest Rate ${x}")
            self.balance += x
            print(f"New Account Balance With Interest Rate: ${self.balance}")
            return self

# * NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    # @classmethod
    # def account_balances(cls):
    #     total = 0
    #     for account in cls.all_accounts:
    #         total += account.balance
    #     return total

david = BankAccount()
david.deposit(10).with_draw(5).with_draw(15).deposit(200).display_account_info().yield_interest()

mowmow = BankAccount()
mowmow.deposit(50).with_draw(10).display_account_info().yield_interest()

# BankAccount.account_balances()