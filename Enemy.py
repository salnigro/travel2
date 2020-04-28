import random


class Enemy(object):
    def __init__(self, level):
        self.name = ""
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.exp = 0
        if level > 2:
            self.level = random.randrange(level-3, level+1)
        else:
            self.level = random.randrange(0, 3)
        self.make()

    def make(self):

        rand = random.randrange(0, 100)
        if rand < 25:
            self.name = "Zombie"
            self.health = 22 + ((self.level - 1) * 4)
            self.attack = 4 + int((self.level - 1) * 1.5)
            self.defense = 8 + int((self.level - 1))
            self.speed = 3 + int((self.level - 1))
            self.exp = int(((30 * self.level) / 7) + .5)
            rand = 200
        if rand < 50:
            self.name = "Skeleton"
            self.health = 13 + int((self.level - 1) * 1.5)
            self.attack = 5 + (self.level - 1)
            self.defense = 13 + int((self.level - 1))
            self.speed = 4 + int((self.level - 1))
            self.exp = int(((30 * self.level) / 7) + .5)
            rand = 200
        if rand < 75:
            self.name = "Goblin"
            self.health = 7 + int((self.level - 1) * .5)
            self.attack = 7 + (self.level - 1)
            self.defense = 15 + int((self.level * 3))
            self.speed = 5 + int((self.level - 1))
            self.exp = int(((30 * self.level) / 7) + .5)
            rand = 200
        if rand < 85:
            self.name = "Ork"
            self.health = 15 + ((self.level - 1) * 1.75)
            self.attack = 9 + int((self.level - 1) * 1.75)
            self.defense = 13 + int((self.level - 1) * 2)
            self.speed = 4 + int((self.level - 1) * .5)
            self.exp = int(((70 * self.level) / 7) + .5)
            rand = 200

        if rand < 95:
            self.name = "black bear"
            self.health = 19 + ((self.level - 1) * 2.5)
            self.attack = 13 + ((self.level - 1) * 2)
            self.defense = 11 + int((self.level - 1) * 1.5)
            self.speed = 6 + int((self.level - 1))
            self.exp = int(((70 * self.level) / 7) + .5)
            rand = 200

        if rand < 100:
            self.name = "Dire wolf"
            self.health = 37 + ((self.level - 1) * 4)
            self.attack = 13 + int((self.level - 1) * 1.5)
            self.defense = 14 + int((self.level - 1) * 1.75)
            self.speed = 7 + int((self.level - 1) * 3)
            self.exp = int(((120 * self.level) / 7) + .5)
