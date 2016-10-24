__author__ = 'john'

class Room:

    def __init__(self, n, name, desc, exits):
        self.number = n
        self.name = name
        self.description = desc
        self.exits = exits
        self.items = []

    def itemToRoom(self, i):
        self.items.append(i)

    def itemFromRoom(self, name):
        for i in self.items:
            if (i.isItem(name)):
                self.items.remove(i)
                return i
        print ("ERROR CAN'T FIND ITEM", name)

    def itemInRoom(self, name):
        for i in self.items:
            if (i.isItem(name)):
                return True
        return False


    def showExits(self):
        s = ""
        if (self.exits[0] > 0):
            s = s + 'n '
        if (self.exits[1] > 0):
            s = s + 's '
        if (self.exits[2] > 0):
            s = s + 'e '
        if (self.exits[3] > 0):
            s = s + 'w '
        if (self.exits[4] > 0):
            s = s + 'u '
        if (self.exits[5] > 0):
            s = s + 'd '
        return s

class World:

    def __init__(self):
        self.rooms = []

    def addRoom(self, r):
        self.rooms.append(r)

    def getDescription(self, n):
        for r in self.rooms:
            if (r.number == n):
                return r.description

    def getRoom(self, n):
        for r in self.rooms:
            if (r.number == n):
#                print "FOUND ROOM", r.description
                return r
        return None

    def itemToRoom(self, i, n):
        self.getRoom(n).itemToRoom(i)

    def move(self, room, dir):
        newRoom = room.number
        if (dir == 'n'):
            newRoom = room.exits[0]
        if (dir == 's'):
            newRoom = room.exits[1]
        if (dir == 'e'):
            newRoom = room.exits[2]
        if (dir == 'w'):
            newRoom = room.exits[3]
        if (dir == 'u'):
            newRoom = room.exits[4]
        if (dir == 'd'):
            newRoom = room.exits[5]

        if (newRoom == 0):
            return room.number
        return newRoom




def initWorld(world):

    # self, n, name, desc, exits
    room1 = Room(1, "Main Street", "Main street of Rockridge", [2, 5, 4, 3, 0, 0])
    room2 = Room(2, "Saloon", "In the saloon", [0, 1, 0, 0, 0, 0])
    room3 = Room(3, "End of the road", "At the end of the road", [0, 0, 1, 0, 0, 0])
    room4 = Room(4, "Graveyard", "In the middle of the Rockridge graveyard",             [0, 0, 0, 1, 0,0])
    room5 = Room(5, "General Store", "In the general store of Rockridge", [ 1, 0, 0, 0, 0, 0])

    world.addRoom(room1)
    world.addRoom(room2)
    world.addRoom(room3)
    world.addRoom(room4)
    world.addRoom(room5)
