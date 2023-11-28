
# * to import the class Pet we do as we did in the below.
# * from pets.py (-> from pets) import the class Pet (-> Pet)
from pets import Pet
# * That would fix the "Pet not defined" but we see that we still have
# * cazador not defined though we imported Pet.. hmmm
# * we can do as such 
# ! from pets import cazador
# * or like line 45 and redefine here. no need for both. but choose wisely.
# personally, to keep code neat you might want to just redefine here and not have it in
# the pets. Think of it as having things organized. It is the Ninja walking the pet.

# * OR WE CAN USE SUPER AS DEMONESTRATED BELOW!!

class Ninja(Pet):
    # * implement __init__( first_name , last_name , treats , pet_food , pet )
    # * implement the following methods:
    # * walk() - walks the ninja's pet invoking the pet play() method
    # * feed() - feeds the ninja's pet invoking the pet eat() method
    # * bathe() - cleans the ninja's pet invoking the pet noise() method

    def __init__(self, first_name, last_name, pets, treats,pet_food):
        super().__init__(pets, treats, pet_food)
        # * why we pass in pets, treats, and pet_food and not name type tricks im not not sure.
        # * im assuming though that it is bc super gets it all and then has pets, treats, pet_food from
        # * coming from Ninja so that they can be tied together and perform properly
        self.first_name = first_name
        self.last_name = last_name
        self.pets = pets 
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(" ")
        print("Walking")
        # cazador.play()
        super().play()
        return self


    def feed(self):
        print(" ")
        print("Feeding")
        super().eat()
        return self

    def bathe(self):
        print(" ")
        print("Bathing")
        # cazador.noise()
        # * with inheritance
        super().noise()
        return self

david = Ninja("David", "Ramirez", "Cazador", "Peanut Butter", "Dog Food")
# cazador=Pet("Cazador", "Pastor Aleman", "Everything")
david.walk().feed().bathe()