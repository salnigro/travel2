from Enemy import Enemy
from Fight import Fight
import random
import tkinter as tk
from tkinter import *
from Player import Player


class Forest(Frame):
    def __init__(self):
        self.cord = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3],
                     [0, 2], [1, 2], [2, 2], [3, 2], [4, 2],
                     [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
                     [0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
                     ]
        self.events = [0, 1, 2, 3, 4,
                       0, 1, 2, 3, 4,
                       0, 1, 2, 3, 4,
                       0, 1, 2, 3, 4]
        random.shuffle(self.events)
        self.pos = [0, 0]
        self.x = 100
        self.y = 400

    def gup(self, player):
        self.root.destroy()
        self.does(player, Enemy(player.level))
        self.pos[1] += 1
        self.x = self.pos[0]*100 + 100
        self.y = 400 - self.pos[1] * 100

        self.move(player, 1)

    def gdown(self, player):
        self.root.destroy()
        self.does(player, Enemy(player.level))
        self.pos[1] -= 1
        self.x = self.pos[0] * 100 + 100
        self.y = 400 - self.pos[1] * 100
        self.move(player, 1)

    def gright(self, player):
        self.root.destroy()
        self.does(player, Enemy(player.level))
        self.pos[0] += 1
        self.x = self.pos[0] * 100 + 100
        self.y = 400 - self.pos[1] * 100
        self.move(player, 1)

    def gleft(self, player):
        self.root.destroy()
        self.does(player, Enemy(player.level))
        self.pos[0] -= 1
        self.x = self.pos[0] * 100 + 100
        self.y = 400 - self.pos[1] * 100
        self.move(player, 1)

    def move(self, player, t):
        if t == 0:
            self.pos = [0, 0]
            self.x = 100
            self.y = 400

        self.root = tk.Tk()
        self.root.geometry("600x500")
        self.frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        self.frame.place(relx=0, rely=0, width=700, height=900)
        canvas = tk.Canvas(self.frame, width=700, height=900, bg='#80c1ff')
        canvas.create_line(100, 100, 100, 400, fill='blue', width=5)
        canvas.create_line(200, 100, 200, 400, fill='blue', width=5)
        canvas.create_line(300, 100, 300, 400, fill='blue', width=5)
        canvas.create_line(400, 100, 400, 400, fill='blue', width=5)
        canvas.create_line(500, 100, 500, 400, fill='blue', width=5)
        canvas.create_line(100, 100, 500, 100, fill='blue', width=5)
        canvas.create_line(100, 200, 500, 200, fill='blue', width=5)
        canvas.create_line(100, 300, 500, 300, fill='blue', width=5)
        canvas.create_line(100, 400, 500, 400, fill='blue', width=5)
        canvas.create_line(100, 500, 500, 500, fill='blue', width=5)
        canvas.create_rectangle(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill='red')
        canvas.pack()
        button = tk.Button(self.frame, text="leave", command=lambda: self.leave(player))
        button.place(relx=0, rely=0, relwidth=.07, relheight=.05)
        for i in range(len(self.cord)):
            if self.pos[0] == self.cord[i][0]:
                if self.pos[1] + 1 == self.cord[i][1]:
                    self.up = tk.Button(self.frame, text="up", command=lambda: self.gup(player))
                    self.up.place(relx=0, rely=.1, relwidth=.07, relheight=.05)
            if self.pos[0] == self.cord[i][0]:
                if self.pos[1] - 1 == self.cord[i][1]:
                    self.down = tk.Button(self.frame, text="down", command=lambda: self.gdown(player))
                    self.down.place(relx=0, rely=.2, relwidth=.07, relheight=.05)
            if self.pos[0] + 1 == self.cord[i][0]:
                if self.pos[1] == self.cord[i][1]:
                    self.right = tk.Button(self.frame, text="right", command=lambda: self.gright(player))
                    self.right.place(relx=0, rely=.3, relwidth=.07, relheight=.05)
            if self.pos[0] - 1 == self.cord[i][0]:
                if self.pos[1] == self.cord[i][1]:
                    self.left = tk.Button(self.frame, text="left", command=lambda: self.gleft(player))
                    self.left.place(relx=0, rely=.4, relwidth=.07, relheight=.05)

        self.root.mainloop()

    def battle(self, player, enemy):
        self.fight = Fight()
        self.fight.start(player, enemy)
        return

    def leave(self, player):
        player.health = player.set
        self.root.destroy()

    def does(self, player, enemy):
        for i in range(len(self.cord)):
            if self.pos == self.cord[i]:
                if self.events[i] < 2:
                    self.battle(player, enemy)
                    break
        return


