print("--Making Object Instances from Dictionary Data--")

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    }
print(kevin["name"])
# output: Kevin Durant

# * Let's say you were receiving data from an 
# * external source like a data base, and wanted 
# * to turn this dictionary data into a Player 
# * object so you could write some useful methods 
# * associated with players. You can imagine just 
# * from the way the dictionary is structured that 
# * you might write your class like this:

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

# * Okay, now that we have a class defined, let's 
# * take our dictionary info to make a Player instance.

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position)
# output: small forward

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

kevin = {"name": "Kevin Durant", "age": 34, "position": "small forward", "team": "Brooklyn Nets"}

# Create a Player instance using the information from the kevin dictionary
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])

# Access the attributes of the player_kevin instance
print(player_kevin.name)
print(player_kevin.age)
print(player_kevin.position)
print(player_kevin.team)