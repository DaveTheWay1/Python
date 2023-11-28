# class Pet:
#     # * implement __init__( name , type , tricks ):
#     # * implement the following methods:
#     # * sleep() - increases the pets energy by 25
#     # * eat() - increases the pet's energy by 5 & health by 10
#     # * play() - increases the pet's health by 5
#     # * noise() - prints out the pet's sound

#     def __init__(self, name, type, tricks):
#         self.name = name
#         self.type = type
#         self.tricks = tricks
#         self.health = 0
#         self.energy = 0

#     def sleep(self):
#         print(" ")
#         print(f"energy before sleeping: {self.energy}")
#         self.energy += 25
#         print(f"energy after sleeping {self.energy}")
#         return self
    
#     def eat(self):
#         print(" ")
#         # print(f"energy before eating: {self.energy}")
#         self.energy += 5
#         self.health += 10
#         print(f"Energy: {self.energy}")
#         print(f"Health: {self.health}")
#         # print(f"energy after eating: {self.energy}")
#         # print(f"health after eating: {self.health}")
#         return self
    
#     def play(self):
#         print(" ")
#         # print(f"health before play: {self.health}")
#         self.health += 5
#         print(f"Health: {self.health}")
#         # print(f"health after playing: {self.health}")
#         return self
    
#     def noise(self):
#         print(" ")
#         print("ARGH ARGH ARGH ARGH ARGHHOOF")

# cazador=Pet("Cazador", "Pastor Aleman", "Everything")
# cazador.sleep().eat().play().noise()
