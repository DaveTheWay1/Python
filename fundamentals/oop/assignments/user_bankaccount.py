# # * The below is the regular assingment. If commented out comment it back in 
# # * if you want to see it but be sure to comment out the sensei version of the 
# # * assingment so that it does not get messy
# class BankAccount:
#     def __init__(self, int_rate, balance):
#         self.int_rate = 0.04
#         self.balance = 0
#         # self.accounts = []

#     def yield_interest(self):
#         if self.balance > 0:
#             x = self.balance * self.int_rate
#             print(f"Total From Interest Rate ${x}")
#             self.balance += x
#             print(f"New Account Balance With Interest Rate: ${self.balance}")
#             return self

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.accounts = BankAccount(int_rate=0.02, balance=0)

# # * Add a make_deposit method to the User class that calls 
# # * on it's bank account's instance methods.

# # dot notation. in our words, in order to acces what is set to equal self.account
# # we use dot notation.
#     def make_deposit(self, amount):
#         self.accounts.balance += amount
#         print(f"New Account Balance: ${self.accounts.balance}")
#         return self

# # * Add a make_withdrawal method to the User class that calls 
# # * on it's bank account's instance methods.

#     def make_withdrawl(self, amount):
#         if self.accounts.balance > amount:
#             self.accounts.balance -= amount
#             print(f"New Account Balance With Withdraw: ${self.accounts.balance}")
#             return self
#         elif self.accounts.balance < amount:
#             print("Insufficient Funds: Charging a $5 fee")
#             self.accounts.balance -= amount
#             self.accounts.balance -= 5
#             print(f"New Account Balance: {self.accounts.balance}")
#             return self

# # * Add a display_user_balance method to the 
# # * User class that displays user's account balance

#     def display_user_balance(self):
#         print(f"Account Balance: ${self.accounts.balance}")
#         return self

# david = User("David", "ramirez@gmail.com")
# david.make_deposit(100).make_withdrawl(13).display_user_balance()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# * SENSEI BONUS: Allow a user to have multiple accounts; 
# * update methods so the user has to specify which account 
# * they are withdrawing or depositing to

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.04
        self.balance = 0

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
        self.accounts = []

    def add_account(self):
            # this was tricky. we were thinking a little too hard.
            # we got too accustomed to creating instances of a class
            # outside of functions so we did not think of
            # creating an instance of a class inside a functoin 
            # until we relaxed our style of thinking.
            new_account = BankAccount(int_rate=0.02, balance=0)
            # we created new_account to refer to the instance of a class.
            self.accounts.append(new_account)
            # with that instance we added it to our list of accounts.
            # since this is all a function - the user can now call it to create 
            # as many accounts as they desire.
            print(self.accounts)
            print("Account Has Been Added!")
            return self
# dot notation. in our words, in order to acces what is set to equal self.account
# we use dot notation.
    def make_deposit(self, account_index, amount):
        # we made it so that our function can now also accept an account_index
        # representing the account the user wishes to refer to.
        if account_index >= 0 and account_index < len(self.accounts):
            # we create an if statement to at least make sure the 
            # user passes in an existing index.
            account = self.accounts[account_index]
            # we make it so that a variable of account can represent 
            # that specific accounts's index.
            account.balance += amount
            print(f"New Account Balance: ${account.balance}")
            # * this could have also been done like the highlighted red below.
            # * the above just also looks slightly cleaner. either or would do.
            # ! self.accounts[account_index].balance += amount
            # ! print(f"New Account Balance: ${self.accounts[account_index].balance}")
        return self

    def make_withdrawl(self, account_index, amount):
        if account_index >= 0 and account_index < len(self.accounts):
            account = self.accounts[account_index]
            if account.balance > amount:
                account.balance -= amount
                print(f"New Account Balance With Withdraw: ${account.balance}")
                return self
            elif account.balance < amount:
                print("Insufficient Funds: Charging a $5 fee")
                account.balance -= amount
                account.balance -= 5
                print(f"New Account Balance: {account.balance}")
                return self

    def display_user_balance(self, account_index):
        if account_index >= 0 and account_index < len(self.accounts):
            account = self.accounts[account_index]
            print(f"Account Balance: ${account.balance}")
            return self
    
    # * SENPAI BONUS: Add a transfer_money(self, amount, other_user) 
    # * method to the user class that takes an amount and a different 
    # * User instance, and transfers money from the user's account 
    # * into another user's account.
    def transfer_money(self,amount, other_user):
        self.make_withdrawl(0,amount)
        print(f"amount withdrawn: ${amount}")
        other_user.make_deposit(0,amount)
        print(f"amount transfered to {other_user.name}: ${amount}")
        return self
    # this was a lot easier with the previous sensei in mind. 
    # practice helps
    # the last sensei helped by allowing me to break down my approach differently
    # just like we created an instance of in object in a function 
    # which was something we haven't normally done
    # we concluding with calling a function within a function


david = User("David", "ramirez@gmail.com")
cazador = User("Cazador", "cazador@gmail.com")
# david.add_account().add_account().make_deposit(0,10).make_withdrawl(0,5).display_user_balance(0).transfer_money(5,cazador)
print(" ")
print(cazador.name)
cazador.add_account().display_user_balance(0)
david.add_account().add_account().make_deposit(0,10).make_withdrawl(0,5).display_user_balance(0).transfer_money(5,cazador)
cazador.display_user_balance(0)

# in order for the transfer to show.. we had to add account to our user
# this could have been avoided though by making it optional to with an if statement
# regardless, we did it this way for now, added a second account so that the fucntion don't get through off
# as it looks for a list but with only one user account and not add account function
# being called for instance object cazador it does not register the list properly
# we call the make transer through instance object david 
# and we then call display_user_balance function so that it displays the object