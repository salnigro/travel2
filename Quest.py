import random


class Quest(object):
    def __init__(self):
        self.gold = 0
        self.exp = 0
        self.task = self.tasks()
        self.cpm = 0

    def tasks(self):
        rand = random.randrange(0, 100)
        if rand < 25:
            self.gold = 5
            self.exp = 10
            return " kill ten zombies "
        if rand < 50:
            self.gold = 5
            self.exp = 10
            return " kill ten skeletons "
        if rand < 75:
            self.gold = 5
            self.exp = 10
            return " kill ten goblins "
        if rand < 90:
            self.gold = 15
            self.exp = 30
            return " kill ten orc "
        if rand < 98:
            self.gold = 15
            self.exp = 30
            return " kill ten black bear "
        if rand < 100:
            self.gold = 40
            self.exp = 70
            return " kill ten dire wolf "

        return rand
