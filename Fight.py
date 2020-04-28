import tkinter as tk
from tkinter import *
from Player import Player
import requests
from PIL import ImageTk, Image


class Fight(object):
    def __init__(self):
        self.rt2 = 0

    def start(self, player, enemy):
        self.battle(player, enemy)
        if self.rt2 == 1:
            return

    def attack(self, player, enemy):
        if player.speed > enemy.speed:
            enemy.health -= int(((2 * player.level) / 5) * (player.attack / enemy.defense) + 2)
            if enemy.health < 1:
                self.celebrate(player, enemy)
            player.health -= int(((2 * enemy.level) / 5) * (enemy.attack / player.defense) + 2)
            if player.health < 1:
                player.health = 0

        else:
            player.health -= int(((2 * enemy.level) / 5) * (enemy.attack / player.defense) + 2)
            if player.health < 1:
                player.health = 0
            else:
                enemy.health -= int(((2 * player.level) / 5) * (player.attack / enemy.defense) + 2)
            if enemy.health < 1:
                self.celebrate(player, enemy)

        self.label1["text"] = "Health: " + str(player.health)
        self.label["text"] = "Health: " + str(enemy.health)
        if player.health < 1:
            self.punish(player)
        return

    def battle(self, player, enemy):
        self.root = tk.Tk()
        canvas = Canvas(self.root, width=400, height=500, bg='#80c1ff')
        canvas.pack()

        img = PhotoImage(master=canvas, file='orc.png')
        img2 = PhotoImage(master=canvas, file='pokemon.png')

        canvas.create_image((50, 50), image=img, state="normal", anchor=NW)
        canvas.create_image((100, 300), image=img2, state="normal", anchor=NW)
        self.label1 = tk.Label(canvas, text="Health: " + str(player.health))
        self.label1.place(x=200, y=400)
        self.label = tk.Label(canvas, text="Health: " + str(enemy.health))
        self.label.place(x=175, y=125)
        self.label2 = tk.Label(canvas, text="name: " + str(enemy.name))
        self.label2.place(x=250, y=125)

        button = tk.Button(canvas, text="attack", command=lambda: self.attack(player, enemy))
        button.place(x=200, y=200)

        self.root.mainloop()

    def celebrate(self, player, enemy):
        self.root.destroy()
        self.root3 = tk.Tk()
        player.exp += enemy.exp
        player.update()
        canvas = Canvas(self.root3, width=400, height=500, bg='#80c1ff')
        canvas.pack()

        img = PhotoImage(master=canvas, file='confetti.png')
        img2 = PhotoImage(master=canvas, file='pokemon.png')

        canvas.create_image((-80, 0), image=img, state="normal", anchor=NW)
        canvas.create_image((100, 300), image=img2, state="normal", anchor=NW)
        label = tk.Label(canvas, text="Good Job!!")
        label.place(x=100, y=100)
        label = tk.Label(canvas, text="Health: " + str(player.health))
        label.place(x=200, y=400)
        button = tk.Button(canvas, text="leave", command=lambda: self.leave())
        button.place(x=200, y=200)
        self.root3.mainloop()

    def leave(self):
        self.root3.destroy()
        self.rt2 = 1

    def punish(self, player):
        player.health = 20
        self.root.destroy()
        return
