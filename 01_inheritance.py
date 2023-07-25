#Parent class
class animal:
    def __init__(self,color,sound,number_of_legs):
        self.color = color
        self.sound = sound
        self.number_of_legs = number_of_legs
    
    def eat(self):
        print("I can eat")
    
    def sound_type(self):
        print("I can",self.sound)
        
    def legs(self):
        print("I have",self.number_of_legs,"legs")
        

#Child class
class Dog(animal):
    def __init__(self,color,sound,number_of_legs):
       animal.__init__(self,color,sound,number_of_legs)
    
    

tom = Dog("Black","bark",4)

tom.eat()
tom.legs()
print(tom.sound)
    
