class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self
    
    def to_the_death_pirate(self, pirate):
        pirate.health = 100
        self.health = 100
        print(f"Pirate Health: {pirate.health} Pirate Strength {pirate.strength}")
        print(f"Ninja Health: {self.health} Ninja Strength {self.strength}")
        while pirate.health > 0 and self.health > 0:
            self.health -= pirate.strength
            pirate.health -= self.strength
            print(f"Pirate Health: {pirate.health}")
            print(f"Ninja Health: {self.health}")
            if self.health < 30 and pirate.health > self.health:
                print("CRITICAL HIT!!!")
                pirate.health -= pirate.health
                print(f"Pirate Health: {pirate.health}")
                print("TKO!!")
        return self