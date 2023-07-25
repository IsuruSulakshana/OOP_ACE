#Grand parent
class House:
    def __init__(self,area,color):
        self.area = area
        self.color = color
    
    def display_info(self):
        print("Color :",self.color)
        print("Area :",self.area)
      
#Parent
class Room(House):
    def __init__(self, area, color, room_type):
        super().__init__(area, color)
        self.room_type = room_type
        
    def display_info(self):
        super().display_info()
        print("Room type :",self.room_type)
        
#Furniture
class Furniture(Room):
    def __init__(self, area, color, room_type, furniture_type):
        super().__init__(area, color, room_type)
        self.furniture_type = furniture_type
    def display_info(self):
        super().display_info()
        print("Furniture type :",self.furniture_type)
        
house_A = House(2500,"White")
house_A.display_info()
print("")
room_A =Room(1000,"Green","Wash room")
room_A.display_info()
print("")
furniture_A = Furniture(250,"Yellow","Bed room","Table")
furniture_A.display_info()