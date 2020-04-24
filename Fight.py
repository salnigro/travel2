import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


class Fight(object):
    def __init__(self, player, enemy):
        self.root2 = tk.Tk()
        self.player = player
        self.enemy = enemy

    def battle(self, player, enemy):
        canvas = Canvas(self.root2, width=300, height=300)
        img = PhotoImage(master=canvas, file='orc.png', width=300, height=300)
        canvas.create_image((50, 50), image=img, state="normal", anchor=NW)
        canvas.pack()

        if enemy.health > 0:
            if player.health > 0:
                if player.speed < enemy.speed:
                    print(enemy.name + " attacks ")
                    player.health -= enemy.attack
                    print("Player health is " + str(player.health))
                else:
                    print("Enemy is a(n) " + enemy.name)
                    t = input(" run or attack ")
                    if t == "attack":
                        enemy.health -= player.attack
                        if enemy.health < 0:
                            enemy.health = 0
                        print(enemy.name + " health is " + str(enemy.health))
                        print(enemy.name + " attacks")
                        player.health -= enemy.attack
                        print("Player health is " + str(player.health))
                        self.battle(player, enemy)
                    else:
                        return

                t = input(" run or attack ")
                if t == "attack":
                    enemy.health -= player.attack
                    if enemy.health < 0:
                        enemy.health = 0
                    print(enemy.name + " health is " + str(enemy.health))
                    self.battle(player, enemy)
                else:
                    return
            else:
                print("player dead")
                print(1 + "t")

        else:
            print("you win")
            print(player.name + " gained " + str(enemy.exp))
            player.exp += 20
            player.update()
        self.root2.mainloop()
        return
