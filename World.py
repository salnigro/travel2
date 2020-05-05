from Town import Town
from Forest import Forest
import math
import tkinter as tk


class World(object):

    def __init__(self, player):
        self.array = []
        self.player = player
        self.c = 0
        self.towns = [Town("Farnfos", [0, 0]), Town("Lunari", [1, 1]),
                      Town("Cewmann", [2, 2]),
                      Town("Caister", [3, 3]), Town("Aramore", [4, 4]),
                      Town("Kilerth", [5, 5]),
                      Town("Eldhams", [6, 6]), Town("Cirrane", [7, 7]),
                      Town("Warcest", [8, 8])]
        self.forest = Forest()

    def menu(self):
        if self.c == 1:
            self.root2.destroy()
        self.c = 0
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
        button = tk.Button(frame, text="Quests", command=lambda: self.quest())
        button.place(relx=0, rely=.2 * 3, relwidth=.5, relheight=.1)
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
        self.forest.move(self.player, 0)
        self.menu()

    def quest(self):
        self.root.destroy()
        self.c = 1
        self.root2 = tk.Tk()
        frame = tk.Frame(self.root2, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        if len(self.player.quest) > 0:
            for i in range(len(self.player.quest)):
                self.label = tk.Label(frame, text=self.player.quest[i], bg='#80c1ff')
                self.label.place(x=0, y=10 + 20 * i)
            button = tk.Button(frame, text="leave", command=lambda: self.menu())
            button.place(relx=.5, y=10, relwidth=.5, relheight=.1)
        else:
            self.label = tk.Label(frame, text="No Quests", bg='#80c1ff')
            self.label.place(x=0, y=0)
            button = tk.Button(frame, text="leave", command=lambda: self.menu())
            button.place(relx=.5, rely=0, relwidth=.5, relheight=.1)
        self.root2.mainloop()
