class House:
    def __init__(self, color, area):
        self.color = color
        self.area = area

    def display_info(self):
        print(f"This is a {self.color} house with an area of {self.area} sq. ft.")


class Room(House):
    def __init__(self, color, area, room_type):
        super().__init__(color, area)
        self.room_type = room_type

    def display_info(self):
        super().display_info()
        print(f"This is a {self.room_type} room.")


class Furniture(Room):
    def __init__(self, color, area, room_type, furniture_type):
        super().__init__(color, area, room_type)
        self.furniture_type = furniture_type

    def display_info(self):
        super().display_info()
        print(f"This room has a {self.furniture_type}.")


# Usage of the House, Room, and Furniture classes
house = House("blue", 1500)
house.display_info()

print("\n")

room = Room("green", 250, "living room")
room.display_info()

print("\n")

furniture = Furniture("yellow", 150, "bedroom", "bed")
furniture.display_info()
