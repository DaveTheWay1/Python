my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

print(" ")
print("--Testing Theory--")
for i in range(0, len(my_list)):
    print(my_list[i])
# samer esult as the first example. The reading wanted to show examples i guess

# while loops
print("--For Loops--")
for count in range(0,5):
    print("looping =", count)
# output:
# looping = 0
# looping = 1
# looping = 2
# looping = 3
# looping = 4

# remember that when we do the range, it does the starting point but it does not do the ending point.
print(" ")
print("--While Loops--")
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

print(" ")
print("--Testing Theory--")
print("--While loop with a range involved--")
count = 0
while count in range(0,5):
    print("looping =", count)
    # ending it at line 42 will cause an infinite loop
    count += 1
    # ending it at like 44 will give you the proper output you desire
# output:
# looping = 0
# looping = 1
# looping = 2
# looping = 3
# looping = 4

# else in a while loop
print("--else in a while loop--")
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

# output:
# 3
# 2
# 1
# Final else statement

print("--Practice--")
y = list("david")
for i in range (0,len(y)):
    print(y[i])
# output:
# d
# a
# v
# i
# d

for i in "david":
    print(i)
# output:
# d
# a
# v
# i
# d

# break
print("--Break--")
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

for val in "David Ramirez":
    if val == " ":
        continue
    print(val)
# output: DavidRamirez 
# skipped the space like expected.

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1

