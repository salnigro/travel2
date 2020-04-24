import random


class Quest(object):
    def __init__(self, gold, exp):
        self.gold = gold
        self.exp = exp
        self.task = self.gtask()
        self.cpm = 0

    def gtask(self):
        rand = random.randrange(0, 2)
        if rand == 0:
            return " kill ten zombies "
        if rand == 1:
            return " kill ten goblins "
        return rand
