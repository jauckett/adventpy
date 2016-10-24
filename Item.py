__author__ = 'john'

global world

# @object
#     @name           computer
#     @title          @a computer
#     @tagline        On top of the desk sits a computer.
#     @description    The computer looks pretty modern--there are two large
#                     LCD monitors connected to it, side-by-side. It's turned
#                     on and there is a sticky note on the desktop: "finish
#                     game." You are a little puzzled.
#     @nouns          computer
#     @carry?         @no It's called a desktop for a reason.

class Item:

    def __init__(self, name, description, nouns, loc):
        self.name = name
        self.description = description
        self.location = loc
        self.nouns = nouns

    # check if the name matches either the name of this item
    # or one of the nouns
    def isItem(self, n):
        if (n == self.name):
            return True
        for noun in self.nouns:
            if (n == noun):
                return True

        return False


class Items:

    def __init__(self):
        self.items = []

    # returns an array of items in a room
    # def findItemsInRoom(self, loc):
    #     tmpItems = []
    #     for i in self.items:
    #         if (loc == i.location):
    #             tmpItems.append(i)
    #     return tmpItems

    def addItem(self, i):
        self.items.append(i)


def initItems(world):
    world.itemToRoom(Item("gun", "Antique flintlock pistol", ["pistol", "gun", "revolver"], 2), 2)
    world.itemToRoom(Item("gunpowder", "Small pile of gunpowder", ["gunpowder", "powder"], 5), 5)
    world.itemToRoom(Item("shot", "Small lead shot ball", ["shot", "lead", "bullet"], 4), 4)

# Item("gun", "Antique flintlock pistol", ["pistol", "gun", "revolver"], 2))
# items.addItem(Item("gunpowder", "Small pile of gunpowder", ["gunpowder", "powder"], 5))
# items.addItem(Item("shot", "Small lead shot ball", ["shot", "lead", "bullet"], 4))
