# CONDITINAL STATEMENTS

x = 12
# variable x is set to the number 12
if x > 50:
    # if x is greater than 50
    print("bigger than 50")
    # print statement display the string
else:
    # else, for in case the if statement did not run, no matter what the else will run.
    print("smaller than 50")
    # print statement displays the string
    # because x is not greater than 50, the second print statement is the only one that will execute
    
x = 55
    # variable x is set to the number 55
if x > 10:
    # if statement, for if x is greater than 10
    print("bigger than 10")
    # if it is then print statement will display the string
elif x > 50:
    # elif in case the if does not run. elif statement for if x is greater than 50.
    print("bigger than 50")
    # if it is then it will display the string
else:
    # else statement for in case neither the if or elif runs.. else will run no matter what
    print("smaller than 10")
    # displays the string
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
if x < 10:
    # if statement for if x is less than 10
    print("smaller than 10")
    # if it is then it will display the string
    # nothing happens, because the statement is false   


# there is also and, or, ==, >=, <=

print("--and--")
i = 10
if i == 10 and i > 5:
    # you cannot just put and > 5... that will result in an error. 
    # must put i again like so ^
    print("i is 10")
else:
    print("try again")
# output: i is 10

print("--or--")
i = 5
if i == 10 or i == 5:
    print("I am not 10 but I am 5")
else:
    print("i am not 5 but i may be 10 or something else")
# output: I am not 10 but I am 5