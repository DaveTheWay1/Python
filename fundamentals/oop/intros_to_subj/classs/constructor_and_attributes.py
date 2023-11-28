# constructor
# It's kind of like when you turn in your completed medical forms to the receptionist. 
# In Python, this is a special function called the __init__ method

# declare a class and give it name User
class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!

print(" ")
print("user ada first name")
user_ada = User()
print(user_ada.first_name) # prints Ada

print(" ")
print("user dave first name")
user_dave = User()
print(user_dave.first_name) # prints Ada

print(" ")
print("accessing user ada last name and age")
print(user_ada.last_name)
print(user_ada.age)

print(" ")
print(f"hi my name is {user_ada.first_name}")
# output: Ada