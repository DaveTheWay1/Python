# try running the code below in order to understand debugging better
# REMINDER: we use PRINT to help us debug

print("--function with unexpected result--")
def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# [2,4,10,16]
print(" ")
print("--breaking down the beginning of code..--")
def multiply(num_list, num): #don't go inside the function until the function is called
    a = [2,4,10,16]
    b = multiply(a,5) # now our function executes; what is a function call equal to?
    print(b) # and the resulting value is printed

print(" ")
print("--using a print at the very beginning of function--")
def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2,4,10,16] 5
# >>>[2,4,10,16]

print(" ")
print("--Testing to see if for loop is working properly--")
def multiply(num_list,num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2, 4, 10, 16] 5
# >>>2
# >>>4
# >>>10
# >>>16
# >>>[2, 4, 10, 16]

print(" ")
print("--Checking If We Are Sucessfully Changing The Value--")
def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(x)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2,4,10,16] 5
# >>>2
# >>>10
# >>>4
# >>>20
# >>>10
# >>>50
# >>>16
# >>>80
# >>>[2, 4, 10, 16]

print(" ")
print("--Is Our Lists Changing?--")
def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2, 4, 10, 16] 5
# >>>2
# >>>[2, 4, 10, 16]
# >>>4
# >>>[2, 4, 10, 16]
# >>>10
# >>>[2, 4, 10, 16]
# >>>16
# >>>[2, 4, 10, 16]

print(" ")
print("--Doing It Correctly--")
def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[10,20,50,80]

# as we can see printing helps see what's going on which can help us nail where we need to make changes
# the reason the code was originally giving us an unepexted result was because we were only multiplying what's in the list.
# instead we needed to multiply what was in the list AND set that to be the value in the list.