class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound"

class Mammal(Animal):
    def nurse(self):
        return "Nursing baby mammals"

class Bird(Animal):
    def fly(self):
        return "Flying in the sky"

class Bat(Mammal, Bird):
    def make_sound(self):
        return "Screech!"

    def activity(self):
        return "Bats are nocturnal animals"

        #      Animal
        #       /   \
        #      /     \
        #   Mammal  Bird
        #      \     /
        #       \   /
        #        Bat

bat = Bat("Batty")
print(bat.name)          # Output: Batty
print(bat.make_sound())  # Output: Screech!
print(bat.nurse())       # Output: Nursing baby mammals
print(bat.fly())         # Output: Flying in the sky
print(bat.activity())    # Output: Bats are nocturnal animals
 