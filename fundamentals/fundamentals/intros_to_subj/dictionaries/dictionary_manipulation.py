person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
print("--original person--")
print(person)

print(" ")
# Adds a new key value pair for email to person
print("--person with adding key of email--")
person["email"] = "alovelace@codingdojo.com"
print(person)

print(" ")
# Changes person's "last" value to "Bobada"
print("--person with changed 'last'--")
person["last"] = "Bobada"
print(person)

print(" ")
print("--to test if a key already exists--")
if "first" in person:
    print(person["first"])
    # output: Ada
print("--using not--")
if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")
# output: Would you like to replace your existing email?

print(" ")
# accessing a value
print("--accesing a value and combing them--")
print(person["first"])
print(person["last"])
full_name = person["first"] + " " + person["last"]
print(full_name)

print(" ")
# removing/deleting a value
print("--removing/deleting--")
value_removed = person.pop('is_organ_donor') # will remove the key 'is_organ_donor' and return it's value
print(value_removed)
# output: True
del person['age'] # will delete the key, and not return anything copy
print(person)
# output: {'first': 'Ada', 'last': 'Bobada', 'email': 'alovelace@codingdojo.com'}

print("--testing pop--")
person.pop("last")
print(person)
# output:{'first': 'Ada', 'email': 'alovelace@codingdojo.com'}
# essentially, if we don't set it to something it is like it is deleting without a return

# print("--testing del--")
# value_removed = del person['first']

# immediately doesn't work storing with del involved. del causes the error

# Multi-Line
person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}

# the above can be written like the below

person = {
    "first": "Ada", 
    "last": "Lovelace", 
    "age": 42, 
    "is_organ_donor": True
}