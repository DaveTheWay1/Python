# Lists 
# Anything can go in a list. Even Lists, tuples, dictionaries, and different datatypes.
ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []


print("--Adding and multiplying lists--")

fruits = ['apple', 'banana', 'orange', 'strawberry']
# a variable of fruits set to a value of a list.
vegetables = ['lettuce', 'cucumber', 'carrots']
# a variable of vegetables set to a value of a list
fruits_and_vegetables = fruits + vegetables
# we create a new variable called fruits and vegetables and set it to the addtion of 
# variables fruits and vegetables. both are lists.
print(" ")
print("--Adding variables fruita and vegetables--")
print(fruits_and_vegetables)
# print statement of the variable fruits_and_vegetables
# output: ['apple', 'banana', 'orange', 'strawberry', 'lettuce', 'cucumber', 'carrots']
print(" ")
print("--Multiplying Variable Vegetables by 3--")
salad = 3 * vegetables
# creating the variable salad and setting it to the result of vegetables times 3
print(salad)
# output: 
# ['lettuce', 'cucumber', 'carrots', 
# 'lettuce', 'cucumber', 'carrots', 
# 'lettuce', 'cucumber', 'carrots']
print(" ")
print("--What Happens If We Add A Single Value To A List--")
tomatoe = "tomatoes"
print("--Result In Error--")
# adding_tomatoe = vegetables + tomatoe
# print(adding_tomatoe)
# output: TypeError: can only concatenate list (not "str") to list
vegetables.append(tomatoe)
print(" ")
print("--Appending--")
print(vegetables)
# ['lettuce', 'cucumber', 'carrots', 'tomatoes']

print(" ")
print("--Converting Tomatoe To List--")
tomatoe_to_list = [tomatoe]
print(tomatoe_to_list)
# output: ['tomatoe']

print(" ")
print("--If We Were To list()--")
adding_tomatoe = vegetables + list(tomatoe)
print(adding_tomatoe)

# output: ['lettuce', 'cucumber', 'carrots', 't', 'o', 'm', 'a', 't', 'o', 'e']

print("--Multiplying Two Different Lists--")
# multiplying_diff_lists = vegetables * fruits
# print(multiplying_diff_lists)

print("--Doesn't Work. Must Be Multiplied By A Number--")

# WE CAN ADD DIFFERENT LISTS TOGETHER BUT CANNOT MULT DIFF LISTS TOGETHER OFC WE CAN ONLY 
# MULTIPLY LISTS BY A NUMBER