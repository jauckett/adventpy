__author__ = 'john'

from Item import *
from World import *
from Character import *
import sys

def help():
    print ("I can't help you sorry.")


# Fix Python 2.x.
try: input = raw_input
except NameError: pass

world = World()
initWorld(world)

# start off in room nunmber 1
inRoom = 1

initItems(world)
character = Character()

while True:
    room = world.getRoom(inRoom)
    print
    print ('-------------------------------------------------------------')
    print (room.description, "(", room.number, ")")
    print ("Visible exits :", room.showExits())

    itemsInRoom = room.items
    if (len(itemsInRoom) > 0):
        print ("Visible items :")
        for i in itemsInRoom:
            print ("    ", i.description)
    cmd = input('>')
    cmd = cmd.lower()

    # check for movement first
    if (cmd in ['n', 's', 'e', 'w', 'u', 'd']):
        newRoom = world.move(room, cmd)
        if (newRoom == inRoom):
            # could not move
            print ("You can't go in that direction!")
        else:
            inRoom = newRoom
        continue

    # check for Inventory command
    if (cmd == 'i'):
        print ("I am carrying :")
        if (len(character.inventory) == 0):
            print ("    Nothing")
            print
        for i in character.inventory:
            print ("   ", i.name)
        continue

    if (cmd == "quit"):
        print ("Bye...")
        sys.exit(0)

    if (cmd == "help"):
        help()
        continue


    # TODO parse the cmd properly

    words = cmd.split(" ")
    if (len(words) > 2):
        print ("I am not that smart, I only understand two word sentences!")
    else:
        if (words[0] in ['take', 'get']):
            if (not room.itemInRoom(words[1])):
                print ("I can't see", words[1], " here!")
                continue
            else:
                r = room.itemFromRoom(words[1])
                character.itemToChar(r)
                print ("Getting", words[1])
                continue
        if (words[0] == 'drop'):
            i = character.itemFromChar(words[1])
            if (i == None):
                print ("You don't have it!")
            else:
                room.itemToRoom(i)
                continue

        print ("Unknown command", cmd)

