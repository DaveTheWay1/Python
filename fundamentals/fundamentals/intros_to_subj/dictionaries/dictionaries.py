#literal notation
person = {"first": "Ada", "last": "Lovelace", 
        "age": 42, "is_organ_donor": True}
capitals = {} #create an empty dictionary

capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

print(person)
# output: {'first': 'Ada', 'last': 'Lovelace', 'age': 42, 'is_organ_donor': True}
print(capitals)
# output: {'svk': 'Bratislava', 'deu': 'Berlin', 'dnk': 'Copenhagen'}

print("--adding to dictionary--")
person["hair"] = "thinning"
print(person)
# output: {'first': 'Ada', 'last': 'Lovelace', 'age': 42, 'is_organ_donor': True, 'hair': 'thinning'}
person["hair"] = "long"
print(person)
# output: {'first': 'Ada', 'last': 'Lovelace', 'age': 42, 'is_organ_donor': True, 'hair': 'long'}