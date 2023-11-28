drawers = ["documents", "envelopes", "pens"]

# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens

# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]

# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]

# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

print(" ")
print("--Try It Yourself--")

things = ["hills", "fresh mornings", "health", "family", "gisselle"]
print("--print health--")
print(things[2])
# output: health
print("--switch hills with gisselle--")
last = "hills"
things[0] = things[4]
things[4] = last
print(things)
# output: ['gisselle', 'fresh mornings', 'health', 'family', 'hills']

print(" ")
print("--Appending Values to a List--")

nums = [1,2,3,4,5]
nums.append(99)
print(nums)
#the output would be [1,2,3,4,5,99]

print(" ")
print("--Slicing--")
words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end'] displays index 1 2 3 4
print(words[:4]) # prints ['start', 'going', 'till', 'the'] displays index 0, 1, 2, 3
print(words[2:4]) # prints ['till', 'the'] displays index 2 and 3. 

print(" ")
print("--Practice--")
slicing = [1,2,3,4,5,6]
print(slicing[0:])
# output: [1, 2, 3, 4, 5, 6]
print(slicing[1:6])
# output: [2, 3, 4, 5, 6]