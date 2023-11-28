# Strings
# Strings are any sequence of characters (letters, numerals, ~($/}\#, etc.) enclosed in single or double quotes
print('--Strings--')
print("this is a sample string")

print(" ")
print("--Practice With Strings--")
print("We are great at printing strings.")

# Concatenating Strings and Variables with the print function
print(" ")
print('--Concactenating w Varibales--')

print(" ")
print("--With Commas--")
name = "Zen"
print("My name is", name)
# output: My name is Zen

print(" ")
print("--Practice with Commas--")
name = "David"
lastName="Ramirez-Vazquez"
print("My name is", name)
print("My first name is", name, "and my last name is", lastName)

print("--Part 2 With Commas--")
print(name, lastName) # natrually with space.. commas better than plus sign so far.

#a different way to do this
print(" ")
print("-- With + --")
name = "Zen"
print("My name is " + name)
# output: My name is Zen
print(" ")
print("--Practice With + --")
name="Gisselle"
lastName="Bonilla-Amaya"
mowMowRealName="Amaris"
print("My name is " + name + " and my last name is " + lastName + ". I have a very nice cat who we call mow mow but his real name is " + mowMowRealName +".")
print(" ")
print("--Part 2 With + --")
print(name + lastName) # Doesn't create Space between first and last name

print(name + " " + lastName) # Creates Space between first and last name

print(" ")
print("--Type Casting or Explicit Type Conversion--")

# print("Hello " + 42) # output: TypeError
print("Hello " + str(42)) # output: Hello 42

print(" ")
print("--Practice--")
print("Hello number", str(362) + "!") #LEARNING!!! a comma would've left a space. 

print("--another exmaple--")
total = 35
user_val = "26"
# total = total + user_val # output: TypeError
total = total + int(user_val) # total will be 61
print(total)
print(" ")
print("--Practice--")
total = 74
num = "26"
print(total + int("26"))

print(" ")
# String Interpolation
print("--String Interpolation--")
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

print(" ")
print("--Practice--")

name = "David"
age = 23
print(f"My name is {name} and I am {age}")

print(" ")
print("--string.format()--")
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

whatIsThis = "Practice"
print(" ")
print("--{}--".format(whatIsThis))

print(" ")
print("--%-formatting--")
hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

print(" ")
print("--Practice--")
thanks = "today I wanted to say to you, %s" % "thanks!" + " " "For all the %d gifts" % 50
print(thanks)

print(" ")
print("--Built-In String Methods--")
x = "hello world"
print(x.title())
# output:
"Hello World"