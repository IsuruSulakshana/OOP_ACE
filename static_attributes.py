class Car:
    num_of_wheels = 4 #static attribute
    
    def __init__(self,make,color):
        self.make = make
        self.color = color
        
    def display_info(self):
        print("Company :",self.make)
        print("color :",self.color)
        print("Number of wheels :", self.num_of_wheels)
           
#print(Car.num_of_wheels)
        
car1 = Car("Toyota","Black")
car1.display_info()

car2 = Car("Honda","Green")
car2.display_info()