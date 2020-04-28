from Npc import Npc
from Town import Town
from Quest import Quest
from Forest import Forest
import math
import tkinter as tk


class World(object):

    def __init__(self, player):
        self.array = []
        self.player = player
        self.npcs = [Npc(), Npc(), Npc(), Npc()]
        self.towns = [Town(self.npcs, "Farnfos", [0, 0]), Town(self.npcs, "Lunari", [1, 1]),
                      Town(self.npcs, "Cewmann", [2, 2]),
                      Town(self.npcs, "Caister", [3, 3]), Town(self.npcs, "Aramore", [4, 4]),
                      Town(self.npcs, "Kilerth", [5, 5]),
                      Town(self.npcs, "Eldhams", [6, 6]), Town(self.npcs, "Cirrane", [7, 7]),
                      Town(self.npcs, "Warcest", [8, 8])]
        self.forest = Forest()

    def menu(self):
        self.root = tk.Tk()
        self.array = []
        start = self.player.location
        for i in range(len(self.towns)):
            st = self.towns[i].location
            if math.sqrt((st[0] - start[0]) * (st[0] - start[0]) + (st[1] - start[1]) * (st[1] - start[1])) < 2:
                self.array.append(self.towns[i].name)

        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        button = tk.Button(frame, text=self.array[0], command=lambda: self.town(self.array[0]))
        button.place(relx=0, rely=.2 * 0, relwidth=.5, relheight=.1)
        button = tk.Button(frame, text=self.array[1], command=lambda: self.town(self.array[1]))
        button.place(relx=0, rely=.2 * 1, relwidth=.5, relheight=.1)
        button = tk.Button(frame, text=self.array[2], command=lambda: self.town(self.array[2]))
        button.place(relx=0, rely=.2 * 2, relwidth=.5, relheight=.1)

        button = tk.Button(frame, text="forest", command=lambda: self.forrest())
        button.place(relx=0, rely=.2 * 4, relwidth=.5, relheight=.1)
        self.root.mainloop()

    def town(self, name):
        self.root.destroy()
        for i in range(len(self.towns)):
            if name == self.towns[i].name:
                self.player.location = self.towns[int(i)].roads[0].start
                self.towns[int(i)].menu(self.player.location, self.player)
                self.player.location = self.towns[int(i)].location

        self.menu()

    def forrest(self):
        self.root.destroy()
        self.forest.move(self.player)
        self.menu()
