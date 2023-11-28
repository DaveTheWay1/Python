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

    # def spend_points(self, amount):
    # have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        if amount <= self.is_rewards_member:
            self.is_rewards_member -= amount
        else: 
            print("insufficient funds brokie!")
        

dave = User("David", "Ramirez", "ramirezdavid@gmail.com", 23)

print(dave.display_info())

print(" ")
dave.enroll()
print(dave.display_info())

print(" ")
print((dave.spend_points(300)))

dave.is_rewards_member = True
print(dave.enroll())
# print(dave.display_info())