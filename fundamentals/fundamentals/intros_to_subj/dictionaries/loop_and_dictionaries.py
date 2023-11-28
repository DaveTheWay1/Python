# for loops
my_dict = { "name": "Noelle", "language": "Python" }
print(my_dict)

print(" ")
print("--accesing keys--")

print(" ")
print("--each_key--")
for each_key in my_dict:
    print(each_key)
# output: name, language

print(" ")
print("--key--")
for key in my_dict:
    print(key)
# output: name, language

print(" ")
print("--using i--")
for i in my_dict:
    print(i)
# output: name, language

# it's all the same.

print(" ")
print("--accessing values--")
my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python

# this makes sense because essentially we are replacing "each_key" with the keys found
# in my dict. so, for example; as we loop and go through the my_dict, name will replace each key
print(" ")
print("--breaking down the previous--")
for each_key in my_dict:
    print(my_dict["name"])
    break
    # we used break just to understand the example. 
    # if not it would've gone through twice and give noelle twice 
    # output: name

print(" ")
print("--have the keys and/or values as the iterator--")
capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"
    }
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc
