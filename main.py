from World import World
from Player import Player
import tkinter as tk


t = Player("name", 1, 10, [5, 5])

world = World(t)

world.menu()
