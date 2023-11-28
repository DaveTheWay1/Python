num1 = 42 
# variable of num1 set to a number
num2 = 2.3
# variable of num2 set to a number.. specefically a float
boolean = True
# varaible of boolean set to a boolean
string = 'Hello World'
# variable of string set to a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable of pizza_toppings set to a list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# variable of person set to a dictionary
fruit = ('blueberry', 'strawberry', 'banana')
# variable of fruit set to a tuple
print(type(fruit))
# print statement of the variable fruit which is a tuple. it will display that tuple
print(pizza_toppings[1])
# print statement of pizza_toppings; a list, specifially Sausage
pizza_toppings.append('Mushrooms')
# print statement of pizza_toppings; a list, appending Mushrooms.. meaning mushrooms will be added to the list
print(person['name'])
# print statement for the variable person; a dictionary, requesting to print by keyword name. will display John
person['name'] = 'George'
# variable person; dictionary, changing the value of the keyword name to George
person['eye_color'] = 'blue'
# person;dictionary, adding a keyword/value to person since eye_color is not an existing key in the dictionary. 
# value set to blue
print(fruit[2])
# print statement for the tuple of fruit. referred by index. displaying banana

if num1 > 45: 
    # if statement checking if num1 is greater than 45
    print("It's greater")
    # if so print statement It's greater will be dsiplayed
else:
    # else statement; if not greater than 45 in this case
    print("It's lower")
    # print statement It's lower will be displayed

if len(string) < 5:
    # if statement checking if the length of string is less than 5
    print("It's a short word!")
    # print statement if the above is true it will display the string
elif len(string) > 15:
    # elif statement checking if the length of string is greater than 15
    print("It's a long word!")
    # print statement will display the string if the first if did not run and if elig results true.
else:
    # else statement which runs no matter what if the above did not run.
    print("Just right!")
    # print statement displays a string

for x in range(5):
    # for loop declared that will go on for every time x is in range of 5
    # x cannot equal 5
    print(x)
    # print statement; x will be displayed.
for x in range(2,5):
    # for loop for every time x is in range between 2 and 5
    # x cannot equal 5
    print(x)
    # print statement will display variable x
for x in range(2,10,3):
    # for loop. for every time x is between 2 and 10 and only runs 3 times.
    # x cannot equal 10 
    print(x)
    # print statement will display the variable x
x = 0
# variable declaration set to a number being 0
while(x < 5):
    # while loop.. while x is less than 5
    print(x)
    # print statmenet will display the variable x
    x += 1
    # x will increase by 1

pizza_toppings.pop()
# pizza_toppings will pop/get rid of the last value in the list.
pizza_toppings.pop(1)
# pizza_toppings will pop/get ris of rid the value in index of 1.

print(person)
# print statment will  print the dictionary of person
person.pop('eye_color')
# person will  pop/get rid of the key eye_color along with its value
print(person)
# print statement will display the dictionary person

for topping in pizza_toppings:
    # a foor loop. this is just like saying for x in pizza_toppings. do no be fooled.
    if topping == 'Pepperoni':
        # if statement checking if topping is peperoni.
        continue
    # if true  it will continue meaning it can move onto checking the next "topping"
    print('After 1st if statement')
    # print statement string
    if topping == 'Olives':
        # if statement checking if  topping is equal to Olives
        break
    # if true it will break meaning 

def print_hello_ten_times():
    # function is declared called ^
    for num in range(10):
        # for loop.. for every  time num is in range of 10
        # num cannot equal 10.
        print('Hello')
        # every time num is in range it will display the string

print_hello_ten_times()
# function is called therefore function will run

def print_hello_x_times(x):
    # function is declared with the name of ^ a parameter of x
    for num in range(x):
        # for loop.. for every time num is in range of x
        print('Hello')
        # print statement will display the string

print_hello_x_times(4)
# function is declared passing in the argument  of a number 4

def print_hello_x_or_ten_times(x = 10):
    # function is delcared with a default parameter of a x set to a number  10
    # default plays a role only if no argument is passed.
    for num in range(x):
        # for loop... for every time num is in range of the parameter x
        print('Hello')
        # print statement will display "Hello"

print_hello_x_or_ten_times()
# function is called.. no arguement is passed so it will run with the default
print_hello_x_or_ten_times(4)
# function is called an argument of 4 is passed so the default  will not run 
# rather the function will run with the number 4 being passed in


"""
Bonus section
"""

num3 = 72
# variable num3 is delcared and set to a number of 72
print(num3)
# print statement displays to variable of num3.  it will display its value.
fruit[0] = 'cranberry'
# fruit; tuple, index 0 is set to cranberry. this will cause an error. Tuples cannot be altered.
print(person['favorite_team'])
# print statement for the dictionary person by keyword favorite_team. nothing will  print as it does not exist nor was it given a value.
print(pizza_toppings[7])
# print statement for pizza toppings list. this will result as an error as there is no value at  the index of 7.
print(boolean)
# print statment for boolean. will display the value of variable boolean
fruit.append('raspberry')
# append for the variable fruit which is a tuple. this results in an error as tuples cannot be altered
fruit.pop(1)
# pop for the varibale fruit. attempting to pop what is int he index of one. but this is a tuple. 
# this will result as an error as tuples cannot be altered.