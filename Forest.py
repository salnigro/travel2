from Enemy import Enemy
import random
import numpy as np
import cv2

class Forest(object):
    def __init__(self):
        self.woods = 1

    def move(self, player):

        pos = [0,0]

        t = input(" left right up down or leave ")
        if t == "t":
            return 0
        if t == "left":
            pos[0] -= 1
        if t == "right":
            pos[0] += 1
        if t == "up":
            pos[1] += 1
        if t == "down":
            pos[0] -= 1
        if t == "leave":
            return 0
        rand = random.randrange(0, 20)

        if rand < 21:
            self.battle(player, Enemy(player.level))
        elif rand < 21:
            print("Found Gold ")
            tr = random.randrange(0, 10)
            print(str(tr))
            player.gold += tr
        self.move()


    def battle(self, player, enemy):
        img = cv2.imread('orc.jpg',0)
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
                        self.move(player)

                t = input(" run or attack ")
                if t == "attack":
                    enemy.health -= player.attack
                    if enemy.health < 0:
                        enemy.health = 0
                    print(enemy.name + " health is " + str(enemy.health))
                    self.battle(player, enemy)
                else:
                    self.move(player)
            else:
                print("player dead")
                print(1 + "t")

        else:
            print("you win")
            print(player.name + " gained " + str(enemy.exp))
            player.exp += 20
            player.update()

        self.move(player)