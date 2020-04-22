from Npc import Npc
from Road import Road
import tkinter as tk


class Town(object):
    def __init__(self, npc, name, location):

        self.array = []
        # self.shop = shop
        self.npc = npc
        self.name = name
        self.location = location
        self.roads = [
            Road("0 rd", [0, 0], 0),
            Road("1 rd", [0, 1], 0),
            Road("2 rd", [0, 2], 0),
            Road("3 rd", [0, 3], 0),
            Road("4 rd", [0, 4], 0),
            Road("5 rd", [1, 4], 0),
            Road("6 rd", [1, 3], 0),
            Road("7 rd", [-1, 3], 0),
            Road("8 rd", [-1, 1], 0),
            Road("9 rd", [1, 2], 0),
        ]

        self.roadp = [
            Road("0 rd", [0, 0], [0, 1]),
            Road("0 rd", [0, 0], [0, 2]),
            Road("0 rd", [0, 0], [0, 3]),
            Road("0 rd", [0, 0], [0, 4]),
            Road("1 rd", [0, 1], [0, 0]),
            Road("1 rd", [0, 1], [0, 2]),
            Road("1 rd", [0, 1], [0, 3]),
            Road("1 rd", [0, 1], [0, 4]),
            Road("1 rd", [0, 1], [-1, 1]),
            Road("2 rd", [0, 2], [0, 0]),
            Road("2 rd", [0, 2], [0, 1]),
            Road("2 rd", [0, 2], [0, 3]),
            Road("2 rd", [0, 2], [0, 4]),
            Road("2 rd", [0, 2], [1, 2]),
            Road("3 rd", [0, 3], [0, 0]),
            Road("3 rd", [0, 3], [0, 1]),
            Road("3 rd", [0, 3], [0, 2]),
            Road("3 rd", [0, 3], [0, 4]),
            Road("3 rd", [0, 3], [-1, 3]),
            Road("4 rd", [0, 4], [0, 0]),
            Road("4 rd", [0, 4], [0, 1]),
            Road("4 rd", [0, 4], [0, 2]),
            Road("4 rd", [0, 4], [0, 3]),
            Road("4 rd", [0, 4], [1, 4]),
            Road("5 rd", [1, 4], [0, 4]),
            Road("5 rd", [1, 4], [1, 3]),
            Road("6 rd", [1, 3], [1, 4]),
            Road("7 rd", [-1, 3], [0, 3]),
            Road("7 rd", [-1, 3], [-1, 1]),
            Road("8 rd", [-1, 1], [-1, 3]),
            Road("8 rd", [-1, 1], [0, 1]),
            Road("9 rd", [1, 2], [0, 2]),
        ]

    # Road("9 rd",[1,2],[2,2]),Road("10 rd",[2,0],[2,2])

    def menu(self, st):
        self.array = []
        self.root = tk.Tk()
        if st == [1, 4]:
            self.npc[0].speech()
        if st == [1, 3]:
            self.npc[1].speech()
        if st == [-1, 3]:
            self.npc[2].speech()
        if st == [1, 2]:
            self.npc[3].speech()
        for i in range(0, len(self.roadp)):
            if st == self.roadp[i].start:
                for j in range(len(self.roadp)):
                    if (self.roadp[i].start == self.roadp[j].end) & (self.roadp[i].end == self.roadp[j].start):
                        s = self.roadp[j].name
                        s = s[0:1]
                        s = int(s)
                        self.array.append(self.roads[s].name)
                        break
        frame = tk.Frame(self.root, bg='#80c1ff', bd=5)
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        for i in range(len(self.array)):
            button = tk.Button(frame, text=self.array[i], command=lambda: self.road(self.array[i]))
            button.place(relx=0, rely=.1 * i, relwidth=.5, relheight=.1)
        self.root.mainloop()

    def road(self, name):
        for i in range(len(self.roads)):
            if name == self.roads[i].name:
                st = self.roads[int(i)].start
                self.menu(st)
