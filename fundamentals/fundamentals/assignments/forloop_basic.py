# Basic - Print all integers from 0 to 150.
print("--0-150--")
for i in range(0, 151):
    # we do a for loop that essentially checks every number(i) within the range of 0-151.
    # we want only to display numbers 0-150. We set it to 151 one though bc as we know
    # it does not reach the last number. if we were to set it to 150 iinstead of 151 it would
    # only display numbers 1-149
    print(i)
# output is all the numbers between 0 and 150

# Print all the multiples of 5 from 5 to 1,000
print("--multiples of 5 from 5 to 1000--")
for i in range(5,1001,5):
    # for loop checking every number from 5-1001, again because we want up to 1000,
    # counting upwards by 5.
    print(i)
    # display all numbers from 5-1000 counting by 5

# Counting, the Dojo Way - Print integers 1 to 100. 
# If divisible by 5, print "Coding" instead. If 
# divisible by 10, print "Coding Dojo".
print("--1 to 100 if / by 5 print coding instead. if / by 10 print coding dojo--")
for i in range(1,101):
    # if statement checking the range for 1-101 because we want from 1-100
    if i % 10 == 0:
        # if statement checking if i is divisible by 10
        # we must set a "== 0" because otherwise it won't really
        # do what we want and won't be checking if divisible by 10
        print("Coding Dojo")
        # print statement will display true if divisible by 10
    elif i % 5 == 0:
        # elif statement checking if divisible by 5
        print("Coding")
        # if so, it will display the string
    else:
        # else statement which will run if neither the if or elif runs
        print(i)
        # displays i

# Whoa. That Sucker's Huge - 
# Add odd integers from 0 to 500,000, and print the final sum.
print("--Addings Odds--")
sum_of_odds = 0 
for i in range(0, 500001):
    if i % 2 != 0:
        sum_of_odds += i
print(sum_of_odds)

print("--Count down from 2018 by 4--")
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range (2018,-1,-4):
    print(i)

# Flexible Counter - Set three variables: lowNum, highNum, mult. 
# Starting at lowNum and going through highNum, print only the 
# integers that are a multiple of mult. For example, if lowNum=2, 
# highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum +1):
    if i % mult == 0:
        print(i)