name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

print("number is",4)

#print("num is" + 4) won't work. only commas work with integers.

num = 4
print("num is", num)


#num = 4
#print("num is" + num)
#the above won't work. must be converted. commas work best in these cases.

print("Hello " + str(42))		# output: Hello 42

total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

print(total)

