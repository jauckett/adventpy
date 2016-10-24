__author__ = 'john'

class Character:

    def __init__(self):
        self.inventory = []


    def itemFromChar(self, name):
        for i in self.inventory:
            if (i.isItem(name)):
                self.inventory.remove(i)
                return i
        return None

    def itemToChar(self, i):
        self.inventory.append(i)

    def hasItem(self, i):
        if (i in self.inventory):
            return True
        return False