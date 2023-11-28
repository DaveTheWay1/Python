import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')


# testing python breakdown || notes

# import random
# -- imports random.

# print('Welcome to Python!')
# -- displays welcome to python as written within the parentheses no quotes.

# print('This is a loop printing 5 times')
# -- displays this is a loop printing 5 times as written within the parentheses no quotes. 

# for x in range(1, 6):
# -- for every time x is in range 1-6. 
# -- the line sets x to 1 automatically and wants it to up to 6.. 

#     print(f'x is: {x}')
# --this is an f string..  will be learned about later. 
# --continuing where we left off, for every time it x is 1-6 do the line above.
# -- the line will print 'x is:' whatever x is.. it will go through each number so there will be a x is 1 x is 2... etc until it hits 6. 6 is still in range of 1-6 so it prints.

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# --we are given a variable called "weekdays" the contains an array of strings of days of the week.

# day = random.choice(weekdays)
# we set a variable of day to equal to the imported "random".choice.. which can be safe to assume that it randomly chooses from the within the parantheses next to it. in this case, it was given the variable weekdays which contains an array of da ys in the week. 
# it will set day to the randomly selected string that exists within the weekdays array.

# print(f'Today is: {day}')
# - another f string. 
# out put of this f string will be 'today is' along with whatever day the random import selected.
# ex: Today is: Monday

# if day == 'Monday':
# if statement. "=" is used to set things equal to something while "==" checks if they are the same.
#     print('It will be a long week!')
# -- if the statement is true it will print the above. 
# elif(day == 'Friday'):
# -- an else if statement stating.. if day has the same value as friday then do the below. this else if only takes action if the first if did not turn out true. 
#     print('Woohoo, time for the weekend!')
# -- if the else if is true then it will print the above.
# else:
# -- else statement. this one runs if none of the other from above run. Always the last one if the previous ones did not turn out true.
#     print('Not quite there yet.')
# if the else runs, the above will be displayed