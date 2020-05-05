import tkinter as tk
from tkinter import *
import random
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
            rand = random.randrange(190, 255)
            enemy.health -= int((((player.level / 5 + 2) * player.attack) / enemy.defense) * (rand / 150))

            if enemy.health < 1:
                self.celebrate(player, enemy)
                enemy.attack = 0
                enemy.level = 0
            rand = random.randrange(160, 255)
            player.health -= int((((enemy.level / 5 + 2) * enemy.attack) / player.defense) * rand / 150)

            if player.health < 1:
                player.health = 0

        else:
            rand = random.randrange(160, 300)

            player.health -= int((((enemy.level / 5 + 2) * enemy.attack) / player.defense) * rand / 150)
            if player.health < 1:
                player.health = 0
            else:
                rand = random.randrange(190, 255)

                enemy.health -= int((((((player.level / 5) + 2) * player.attack) / enemy.defense) * rand / 150))
            if enemy.health < 1:
                self.celebrate(player, enemy)

        self.label1["text"] = "Health: " + str(player.health)
        self.label["text"] = "Health: " + str(enemy.health)
        if player.health < 1:
            self.punish(player)
        return

    def battle(self, player, enemy):
        self.root = tk.Tk()
        canvas = Canvas(self.root, width=600, height=500, bg='#80c1ff')
        canvas.pack()
        img = PhotoImage(master=canvas, file='orc.png')
        if enemy.name == "Zombie":
            img = PhotoImage(master=canvas, file='zombie.png')
        if enemy.name == "Skeleton":
            img = PhotoImage(master=canvas, file='skeleton.png')
        if enemy.name == "Goblin":
            img = PhotoImage(master=canvas, file='goblin.png')
        if enemy.name == "Orc":
            img = PhotoImage(master=canvas, file='orc.png')
        if enemy.name == "Black bear":
            img = PhotoImage(master=canvas, file='bear.png')
        if enemy.name == "Dire wolf":
            img = PhotoImage(master=canvas, file='wolf.png')
        img2 = PhotoImage(master=canvas, file='pokemon.png')

        canvas.create_image((250, 100), image=img, state="normal", anchor=NW)
        canvas.create_image((250, 300), image=img2, state="normal", anchor=NW)
        self.label1 = tk.Label(canvas, text="Health: " + str(player.health), bg='#80c1ff')
        self.label1.place(x=200, y=400)
        self.label = tk.Label(canvas, text="Health: " + str(enemy.health), bg='#80c1ff')
        self.label.place(x=300, y=200)
        self.label3 = tk.Label(canvas, text="Level: " + str(enemy.level), bg='#80c1ff')
        self.label3.place(x=250, y=200)
        self.label2 = tk.Label(canvas, text=str(enemy.name), bg='#80c1ff')
        self.label2.place(x=275, y=75)

        button = tk.Button(canvas, text="Attack", command=lambda: self.attack(player, enemy))
        button.place(x=400, y=400)
        button = tk.Button(canvas, text="Run away", command=lambda: self.run())
        button.place(x=450, y=400)
        self.root.mainloop()

    def celebrate(self, player, enemy):
        self.root.destroy()
        self.root3 = tk.Tk()
        for i in range(len(player.quest)):
            if player.quest[i] == " kill ten zombies ":
                if enemy.name == "Zombie":
                    player.counter[i] += 5
                    print(player.counter[i])
            if player.quest[i] == " kill ten skeletons ":
                if enemy.name == "Skeleton":
                    player.counter[i] += 1
                    print(player.counter[i])
            if player.quest[i] == " kill ten goblins ":
                if enemy.name == "Goblin":
                    player.counter[i] += 1
                    print(player.counter[i])
            if player.quest[i] == " kill ten orcs ":
                if enemy.name == "Orc":
                    player.counter[i] += 1
                    print(player.counter[i])
            if player.quest[i] == " kill ten black bears ":
                if enemy.name == "Black bear":
                    player.counter[i] += 1
            if player.quest[i] == " kill ten dire wolves ":
                if enemy.name == "Dire wolf":
                    player.counter[i] += 1
        player.exp += enemy.exp

        canvas = Canvas(self.root3, width=400, height=500, bg='#80c1ff')
        canvas.pack()
        player.update()
        img = PhotoImage(master=canvas, file='confetti.png')
        img2 = PhotoImage(master=canvas, file='pokemon.png')

        canvas.create_image((-80, 0), image=img, state="normal", anchor=NW)
        canvas.create_image((100, 300), image=img2, state="normal", anchor=NW)
        label = tk.Label(canvas, text="Good Job!!", bg='#80c1ff')
        label.place(x=150, y=10)
        label = tk.Label(canvas, text="level: " + str(player.level), bg='#80c1ff')
        label.place(x=100, y=50)
        label = tk.Label(canvas, text="Health: " + str(player.health), bg='#80c1ff')
        label.place(x=175, y=50)
        label = tk.Label(canvas, text="Attack: " + str(player.attack), bg='#80c1ff')
        label.place(x=100, y=75)
        label = tk.Label(canvas, text="Defense: " + str(player.defense), bg='#80c1ff')
        label.place(x=175, y=75)
        label = tk.Label(canvas, text="Speed: " + str(player.speed), bg='#80c1ff')
        label.place(x=100, y=100)
        label = tk.Label(canvas, text="EXP: " + str(player.exp), bg='#80c1ff')
        label.place(x=175, y=100)
        label = tk.Label(canvas, text="You gained " + str(enemy.exp) + " exp", bg='#80c1ff')
        label.place(x=150, y=30)
        button = tk.Button(canvas, text="Leave", command=lambda: self.leave(), bg='#80c1ff')
        button.place(x=150, y=300)
        self.root3.mainloop()

    def leave(self):
        self.root3.destroy()
        self.rt2 = 1

    def run(self):
        self.root.destroy()

    def punish(self, player):
        player.health = 20
        self.root.destroy()
        return
