from decimal import *
import tkinter as tk
from Quest import Quest


class Player(object):

    def __init__(self, name, level, gold, location):
        self.exp = 0
        self.name = name
        self.level = level
        self.gold = gold
        self.location = location
        self.health = 20
        self.attack = 8
        self.defense = 10
        self.speed = 5
        self.set = 20
        self.counter = []
        self.quest = []

    def update(self):

        t = int(((Decimal(1.6363319771444 ** -6) * (self.level ** 4)) -
                 Decimal(2.3500018552718 ** -4) * (self.level ** 3)
                 + Decimal(2.4081865400999) * (self.level ** 2) +
                 Decimal(2.3038650142963) * self.level + Decimal(1.1160666419851)) +
                Decimal(.5))
        if self.exp > t:
            self.level += 1
            self.set += 10
            self.attack += 3
            self.defense += 2
            self.speed += 2
            self.exp = self.exp - t
            self.health = self.set

