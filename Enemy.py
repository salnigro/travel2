import random


class Enemy(object):
    def __init__(self, level):
        self.name = ""
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.exp = 0
        if level > 1:
            self.level = random.randrange(level, level+3)
        else:
            self.level = 1
        self.make()
    def make(self):

        rand = random.randrange(0, 100)
        if rand < 85:
            self.name = "Zombie"
            self.health = 10 + ((self.level-1))
            self.attack = 6 + ((self.level-1) * 2)
            self.defense = 3 + int((self.level-1) * .5)
            self.speed = 4 + int((self.level-1) * 5)
            self.exp = int(((30 * self.level) / 7) + .5)
        if rand < 100:
            self.name = "Ork"
            self.health = 15 + ((self.level-1) * 4)
            self.attack = 4 + ((self.level-1) * 3)
            self.defense = 5 + int((self.level-1))
            self.speed = 2 + int((self.level-1) * .5)
            self.exp = int(((70 * self.level) / 7) + .5)

