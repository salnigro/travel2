from Enemy import Enemy
from Test import Test
from Fight import Fight
import random
import tkinter as tk
from tkinter import *
from Player import Player


class Forest(Frame):
    def __init__(self):
        self.pos = [0, 0]
        self.woods = 1

    def left(self, player):
        self.pos[0] -= 1

        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr

    def up(self, player):
        self.pos[1] += 1

        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr

    def down(self, player):
        self.pos[1] -= 1

        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr

    def right(self, player):
        self.pos[0] += 1
        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr

    def move(self, player):
        self.root = tk.Tk()
        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        button = tk.Button(frame, text="left", command=lambda: self.left(player))
        button.place(relx=0, rely=.2 * 0, relwidth=.5, relheight=.1)
        button = tk.Button(frame, text="right", command=lambda: self.right(player))
        button.place(relx=0, rely=.2 * 1, relwidth=.5, relheight=.1)
        button = tk.Button(frame, text="up", command=lambda: self.up(player))
        button.place(relx=0, rely=.2 * 2, relwidth=.5, relheight=.1)
        button = tk.Button(frame, text="down", command=lambda: self.down(player))
        button.place(relx=0, rely=.2 * 3, relwidth=.5, relheight=.1)
        button = tk.Button(frame, text="leave", command=lambda: self.leave())
        button.place(relx=0, rely=.2 * 4, relwidth=.5, relheight=.1)

        self.root.mainloop();

    def battle(self, player, enemy):
        self.root.destroy()
        self.fight = Fight()
        self.fight.start(player, enemy)
        self.move(player)

    def leave(self):
        self.root.destroy()
