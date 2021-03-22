# Author Lauri Putkonen
# House with 3 Rooms (note: composition)

class House:
    def __init__(self):
        self.rooms = 0
        self.squares = 0
        self.roomNames = []

    def addRoom(self, room):
        self.rooms += 1
        self.squares += room.sqr
        self.roomNames.append(room.room_name)

    def print_house(self):
        print("The house has", self.rooms, "rooms and", self.squares, "squares")

    def print_rooms(self):
        print(self.roomNames)
        
        
class Room:
    def __init__(self, room_name, width, length):
        self.room_name = room_name
        self.width = width
        self.length = length
        self.sqr = width * length
        
apartment = House()
kitchen = Room("Kitchen", 4, 5)
apartment.addRoom(kitchen)

livingRoom = Room("Living room", 5, 5)
apartment.addRoom(livingRoom)

bathroom = Room("Bathroom", 3, 2.5)
apartment.addRoom(bathroom)

apartment.print_house()
apartment.print_rooms()

#OUTPUT:
# The house has 3 rooms and 52.5 squares
# ['Kitchen', 'Living room', 'Bathroom']


    
