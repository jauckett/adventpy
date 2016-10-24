__author__ = 'john'

global world

class Item:

    def __init__(self, name, description, nouns):
        self.name = name
        self.description = description
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

    def addItem(self, i):
        self.items.append(i)


def initItems(world):
    world.itemToRoom(Item("gun", "Antique flintlock pistol", ["pistol", "gun", "revolver"]), 2)
    world.itemToRoom(Item("gunpowder", "Small pile of gunpowder", ["gunpowder", "powder"]), 5)
    world.itemToRoom(Item("shot", "Small lead shot ball", ["shot", "lead", "bullet", "ball"]), 4)


