# Author Lauri Putkonen
# House with 3 Rooms (note: composition)

class House:
    def __init__(self):
        self.squares = 0
        self.rooms = []

    def addRoom(self, room):
        self.squares += room.sqr
        self.rooms.append(room)

    def __str__(self):
        return "The house has " + str(len(self.rooms)) + " rooms and " + str(self.squares) + " squares"

    def printAllRooms(self):
        for i in range(len(self.rooms)):
            print(self.rooms[i].room_name + ", " + str(self.rooms[i].sqr) + "m2")
        
        
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

print(apartment)
apartment.printAllRooms()

#OUTPUT:
# The house has 3 rooms and 52.5 squares
# Kitchen, 20m2
# Living room, 25m2
# Bathroom, 7.5m2


    
