
# * Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) 
# that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, 
# and then prints the associated values within each key's list. 
# For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

num_locations = len(dojo["locations"])
print(f"{num_locations} LOCATIONS")

for i in range(0,len(dojo["locations"])):
    print(dojo["locations"][i])


print(" ")


num_instructors = len(dojo["instructors"])
print((f"{num_instructors} INSTRUCTORS"))

for i in range(0,len(dojo["instructors"])):
    print(dojo["instructors"][i])
