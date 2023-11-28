# Chaining Methods

class User: 
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print(" ")
        return self

    # def enroll(self):
    #  Have this method change the user's member status to True and set their gold card points to 200.
    # def enroll(self):
    #     self.is_rewards_member = True
    #     self.gold_card_points += 200
    # Ninja Bonuses:
    # Add logic in the enroll method to check if they 
    # are a member already, and if they are, print 
    # "User already a member." and return False, 
    # otherwise return True.
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
            print(f"Total Gold Card Points: {self.gold_card_points}")
            print(" ")
        return self

    # def spend_points(self, amount):
    # have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        print(f"amount: {amount}")
        print(" ")
        if amount < self.gold_card_points:
            print(" ")
            print(amount)
            print(" ")
            self.gold_card_points -= amount
            return self
        else: 
            print("insufficient funds brokie!")
        return self
#error 
# dave.display_info().enroll().spend_points(50).display_info()
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'bool' object has no attribute 'display_info'

# we had an error here. we would try to return True or False instead of self. We even tried amount here.
# the errror we were getting was for the last display_info() of the chaining method
# neither were accurate. we got confused until we tried to return self
# self works and is the only appropiate return because it allows us to continue the chaining method
# returning anything else does not return the instance object which is what we require,
# self refers to the instance. amount does not as it refers to the amount specifically.
# true or false does not as it refers to the outcome. we need self for the chaining method
# so it can continue to pass it through the chaining method
dave = User("David", "Ramirez", "ramirezdavid@gmail.com", 23)


# instead of doing the above, calling a method on seperate lines, we can do the below ex:
# user1.display_info().enroll().spend_points(50).display_info()
# user2.enroll().spend_points(80).display_info()

dave.display_info().enroll().spend_points(50).display_info()