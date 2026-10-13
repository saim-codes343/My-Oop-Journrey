class Player:
    def __init__(self,name):
        self.name = name
        self.items = ['Sword']

    def __str__(self):
        return f"Name: {self.name}\nItems: {', '.join(self.items)}"

from copy import *
p1 = Player('Ali')
p2 = copy(p1)
p2.name = 'Sara'
p1.items.append('Shield')
print(p1)
print(p2)
p3 = deepcopy(p1)
p3.items.append('Bow')
print(p1)
print(p3)        