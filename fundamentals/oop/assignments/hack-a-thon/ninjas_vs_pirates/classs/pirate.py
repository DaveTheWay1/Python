class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self
    
    def death_to_ninja(self, ninja):
        ninja.health = 100
        self.health = 100
        print(f"Pirate Health: {ninja.health} Pirate Strength {ninja.strength}")
        print(f"Ninja Health: {self.health} Ninja Strength {self.strength}")
        while ninja.health > 0 and self.health > 0:
            ninja.health -= self.strength
            self.health -= ninja.strength
            print(f"Ninja Health: {ninja.health}")
            print(f"Pirate Health: {self.health}")
        return self