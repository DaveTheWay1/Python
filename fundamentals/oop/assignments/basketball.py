# # * Challenge 1: Update the Constructor
# # class Player:
# #     def __init__(self, name, age, position, team):
# #         self.name = name
# #         self.age = age
# #         self.position = position
# #         self.team = team

# # * Update the constructor to accept a 
# # * dictionary with a single player's 
# # * information instead of individual 
# # * arguments for the attributes.

class Player:
    def __init__(self, player_data):
        self.name = player_data["name"]
        self.age = player_data["age"]
        self.position = player_data["position"]
        self.team = player_data["team"]
    # * Ninja Bonus: Add an @class method called get_team(cls, team_list) 
    # * that, given a list of dictionaries populates and returns 
    # * a new list of Player objects.
    @classmethod
    def get_team(cls, team_list):
        newteam_list = []
        for player in range(len(team_list)):
            newteam_list.append(team_list[player]["team"])
        return newteam_list
    
    # * Complete challenge 3: Populate a new list with Player 
    # * instances from the list of players.
    @classmethod
    def creating_list(cls):
        new_list = []
        for player in range(len(players)-1):
            print(players[player]["name"])
            new_list.append(players[player]["name"])
        return new_list

# Create instances using individual player dictionaries
kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
# # * Challenge 2: Create instances using individual player dictionaries.
kevin_player = Player(kevin)
jason_player = Player(jason)
kyrie_player = Player(kyrie)

# List of player dictionaries
players = [
    {
        "name": "Kevin Durant", 
        "age": 34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age": 24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age": 32, 
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age": 33, 
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age": 32, 
        "position": "Power Forward", 
        "team": "Philadelphia 76ers"
    },
    {
        "name": "", 
        "age": 16, 
        "position": "P", 
        "team": "en"
    }
]
print(f"new List: {Player.creating_list()}")
# Call the class method using Player.get_team(players)
team_list = Player.get_team(players)
print(f"Teams: {team_list}")
